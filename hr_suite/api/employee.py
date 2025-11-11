import frappe
from frappe import _
from frappe.utils import today, add_days, getdate
from datetime import datetime

@frappe.whitelist()
def after_employee_insert(doc, method):
    """
    Triggered after employee is created
    """
    # Send welcome email
    send_welcome_email(doc)
    
    # Create user account if email provided
    if doc.company_email:
        create_user_account(doc)
    
    # Allocate leaves
    allocate_leaves(doc)
    
    # Assign default shift
    assign_default_shift(doc)

def send_welcome_email(employee):
    """
    Send welcome email to new employee
    """
    if not employee.company_email:
        return
        
    try:
        frappe.sendmail(
            recipients=employee.company_email,
            subject=f"Welcome to {frappe.defaults.get_defaults().company}",
            template="Welcome Email - New Employee",
            args={"doc": employee},
            reference_doctype="Employee",
            reference_name=employee.name,
            now=True
        )
        frappe.msgprint(_(f"Welcome email sent to {employee.employee_name}"), alert=True)
    except Exception as e:
        frappe.log_error(f"Failed to send welcome email to {employee.name}: {str(e)}")

def create_user_account(employee):
    """
    Create user account for employee with self-service access
    """
    if not employee.company_email:
        return
        
    if frappe.db.exists("User", employee.company_email):
        # User already exists, just link it
        employee.user_id = employee.company_email
        employee.save(ignore_permissions=True)
        return
        
    try:
        user = frappe.get_doc({
            "doctype": "User",
            "email": employee.company_email,
            "first_name": employee.first_name,
            "last_name": employee.last_name or "",
            "send_welcome_email": 1,
            "user_type": "System User",
            "enabled": 1
        })
        user.insert(ignore_permissions=True)
        
        # Assign Employee Self Service role
        user.add_roles("Employee Self Service", "Employee")
        
        # Link user to employee
        employee.user_id = user.name
        employee.save(ignore_permissions=True)
        
        frappe.msgprint(_(f"User account created for {employee.employee_name}"), alert=True)
        
    except Exception as e:
        frappe.log_error(f"Failed to create user for employee {employee.name}: {str(e)}")

def allocate_leaves(employee):
    """
    Auto-allocate leaves to new employee
    """
    try:
        # Get all active leave types
        leave_types = frappe.get_all("Leave Type", 
            filters={"is_active": 1},
            fields=["name", "max_leaves_allowed", "applicable_after"]
        )
        
        joining_date = getdate(employee.date_of_joining)
        current_year_start = datetime(datetime.now().year, 1, 1).date()
        current_year_end = datetime(datetime.now().year, 12, 31).date()
        
        for leave_type in leave_types:
            # Check if allocation already exists
            if frappe.db.exists("Leave Allocation", {
                "employee": employee.name,
                "leave_type": leave_type.name,
                "from_date": current_year_start
            }):
                continue
                
            # Calculate allocation date based on applicable_after
            allocation_from_date = max(
                joining_date,
                current_year_start
            )
            
            if leave_type.applicable_after:
                allocation_from_date = max(
                    allocation_from_date,
                    add_days(joining_date, leave_type.applicable_after)
                )
            
            # Only allocate if applicable date is within current year
            if allocation_from_date <= current_year_end:
                try:
                    allocation = frappe.get_doc({
                        "doctype": "Leave Allocation",
                        "employee": employee.name,
                        "employee_name": employee.employee_name,
                        "leave_type": leave_type.name,
                        "from_date": allocation_from_date,
                        "to_date": current_year_end,
                        "new_leaves_allocated": leave_type.max_leaves_allowed or 0,
                        "description": "Auto-allocated on joining"
                    })
                    allocation.insert(ignore_permissions=True)
                    allocation.submit()
                    
                except Exception as e:
                    frappe.log_error(f"Failed to allocate {leave_type.name} for {employee.name}: {str(e)}")
        
        frappe.msgprint(_(f"Leaves allocated for {employee.employee_name}"), alert=True)
                    
    except Exception as e:
        frappe.log_error(f"Failed to allocate leaves for employee {employee.name}: {str(e)}")

def assign_default_shift(employee):
    """
    Assign default shift to employee
    """
    try:
        # Check if General Shift exists
        if not frappe.db.exists("Shift Type", "General Shift"):
            return
            
        # Check if shift assignment already exists
        if frappe.db.exists("Shift Assignment", {
            "employee": employee.name,
            "status": "Active"
        }):
            return
        
        shift_assignment = frappe.get_doc({
            "doctype": "Shift Assignment",
            "employee": employee.name,
            "employee_name": employee.employee_name,
            "shift_type": "General Shift",
            "start_date": employee.date_of_joining,
            "status": "Active"
        })
        shift_assignment.insert(ignore_permissions=True)
        shift_assignment.submit()
        
    except Exception as e:
        frappe.log_error(f"Failed to assign shift for employee {employee.name}: {str(e)}")

@frappe.whitelist()
def get_employee_details(employee_id):
    """
    Get comprehensive employee details
    """
    if not frappe.has_permission("Employee", "read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    employee = frappe.get_doc("Employee", employee_id)
    
    # Get leave balance
    leave_balance = get_leave_balance(employee_id)
    
    # Get recent attendance
    recent_attendance = get_recent_attendance(employee_id)
    
    return {
        "employee": employee.as_dict(),
        "leave_balance": leave_balance,
        "recent_attendance": recent_attendance
    }

def get_leave_balance(employee_id):
    """
    Get leave balance for all leave types
    """
    from frappe.utils import get_first_day, get_last_day
    
    leave_types = frappe.get_all("Leave Type", filters={"is_active": 1}, pluck="name")
    balance = {}
    
    for leave_type in leave_types:
        try:
            from erpnext.hr.doctype.leave_application.leave_application import get_leave_balance_on
            bal = get_leave_balance_on(
                employee_id,
                leave_type,
                today()
            )
            balance[leave_type] = bal
        except:
            balance[leave_type] = 0
    
    return balance

def get_recent_attendance(employee_id, days=30):
    """
    Get recent attendance records
    """
    from_date = add_days(today(), -days)
    
    attendance = frappe.get_all("Attendance",
        filters={
            "employee": employee_id,
            "attendance_date": [">=", from_date]
        },
        fields=["attendance_date", "status", "in_time", "out_time"],
        order_by="attendance_date desc"
    )
    
    return attendance