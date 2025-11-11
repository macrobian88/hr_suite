import frappe
from frappe import _

def after_employee_insert(doc, method):
    """
    Triggered after employee is created
    """
    # Send welcome email
    send_welcome_email(doc)
    
    # Create user account
    create_user_account(doc)
    
    # Allocate leaves
    allocate_leaves(doc)

def send_welcome_email(employee):
    """Send welcome email to new employee"""
    try:
        frappe.sendmail(
            recipients=employee.company_email,
            subject=f"Welcome to {frappe.defaults.get_defaults().company}",
            template="Welcome Email",
            args={"doc": employee},
            reference_doctype="Employee",
            reference_name=employee.name
        )
    except Exception as e:
        frappe.log_error(f"Failed to send welcome email: {str(e)}")

def create_user_account(employee):
    """Create user account for employee"""
    if not employee.user_id and employee.company_email:
        try:
            user = frappe.get_doc({
                "doctype": "User",
                "email": employee.company_email,
                "first_name": employee.first_name,
                "last_name": employee.last_name,
                "send_welcome_email": 1,
                "user_type": "System User"
            })
            user.insert(ignore_permissions=True)
            
            # Assign Employee Self Service role
            user.add_roles("Employee Self Service")
            
            employee.user_id = user.name
            employee.save(ignore_permissions=True)
            
        except Exception as e:
            frappe.log_error(f"Failed to create user: {str(e)}")

def allocate_leaves(employee):
    """Auto-allocate leaves to new employee"""
    from datetime import datetime
    
    try:
        # Get all active leave types
        leave_types = frappe.get_all("Leave Type", 
            filters={"is_active": 1},
            fields=["name", "max_leaves_allowed"]
        )
        
        for leave_type in leave_types:
            if not frappe.db.exists("Leave Allocation", {
                "employee": employee.name,
                "leave_type": leave_type.name
            }):
                allocation = frappe.get_doc({
                    "doctype": "Leave Allocation",
                    "employee": employee.name,
                    "leave_type": leave_type.name,
                    "from_date": datetime.now().date(),
                    "to_date": datetime(datetime.now().year, 12, 31).date(),
                    "new_leaves_allocated": leave_type.max_leaves_allowed or 0,
                    "description": "Auto-allocated on joining"
                })
                allocation.insert(ignore_permissions=True)
                allocation.submit()
                
    except Exception as e:
        frappe.log_error(f"Failed to allocate leaves: {str(e)}")