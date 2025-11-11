import frappe
from frappe.utils import today, add_days

def daily_hr_reminders():
    """Send daily HR reminders"""
    
    # Birthday reminders
    send_birthday_reminders()
    
    # Probation ending reminders
    send_probation_reminders()
    
    # Leave balance reminders
    send_leave_balance_reminders()

def send_birthday_reminders():
    """Send birthday wishes"""
    from datetime import datetime
    
    today_date = datetime.now().strftime("%m-%d")
    
    employees = frappe.get_all("Employee",
        filters={
            "status": "Active",
            "date_of_birth": ["like", f"%{today_date}"]
        },
        fields=["name", "employee_name", "company_email", "user_id"]
    )
    
    for emp in employees:
        if emp.user_id:
            try:
                # Send birthday notification
                frappe.publish_realtime(
                    event="msgprint",
                    message=f"🎉 Happy Birthday {emp.employee_name}!",
                    user=emp.user_id
                )
                
                # Notify HR
                hr_users = frappe.get_all("User", 
                    filters={"name": ["in", frappe.get_roles()]},
                    pluck="name"
                )
                
                for hr_user in hr_users:
                    frappe.publish_realtime(
                        event="msgprint",
                        message=f"🎂 Today is {emp.employee_name}'s birthday!",
                        user=hr_user
                    )
                    
            except Exception as e:
                frappe.log_error(f"Failed to send birthday reminder: {str(e)}")

def send_probation_reminders():
    """Remind HR about probation ending"""
    upcoming_date = add_days(today(), 7)
    
    employees = frappe.get_all("Employee",
        filters={
            "status": "Active",
            "final_confirmation_date": upcoming_date
        },
        fields=["name", "employee_name", "final_confirmation_date"]
    )
    
    if employees:
        # Get HR Managers
        hr_managers = frappe.get_all("User",
            filters={
                "enabled": 1,
                "name": ["in", frappe.get_roles("HR Manager Suite")]
            },
            pluck="name"
        )
        
        message = "Probation ending in 7 days for:<br>"
        for emp in employees:
            message += f"- {emp.employee_name} ({emp.final_confirmation_date})<br>"
        
        for manager in hr_managers:
            try:
                frappe.publish_realtime(
                    event="msgprint",
                    message=message,
                    user=manager
                )
            except Exception as e:
                frappe.log_error(f"Failed to send probation reminder: {str(e)}")

def send_leave_balance_reminders():
    """Remind employees about leave balance"""
    from datetime import datetime
    
    # Send quarterly reminders (1st day of Jan, Apr, Jul, Oct)
    if datetime.now().day == 1 and datetime.now().month in [1, 4, 7, 10]:
        
        employees = frappe.get_all("Employee",
            filters={"status": "Active"},
            fields=["name", "employee_name", "user_id"]
        )
        
        for emp in employees:
            if emp.user_id:
                try:
                    # Get leave balance
                    leave_allocations = frappe.get_all("Leave Allocation",
                        filters={
                            "employee": emp.name,
                            "docstatus": 1,
                            "to_date": [">=", today()]
                        },
                        fields=["leave_type", "total_leaves_allocated", "leaves_taken"]
                    )
                    
                    if leave_allocations:
                        message = f"Your leave balance:<br>"
                        for leave in leave_allocations:
                            balance = leave.total_leaves_allocated - leave.leaves_taken
                            message += f"- {leave.leave_type}: {balance} days<br>"
                        
                        frappe.publish_realtime(
                            event="msgprint",
                            message=message,
                            user=emp.user_id
                        )
                        
                except Exception as e:
                    frappe.log_error(f"Failed to send leave balance reminder: {str(e)}")
