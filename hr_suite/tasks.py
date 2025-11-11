import frappe
from frappe import _
from frappe.utils import today, add_days, getdate, get_first_day
from datetime import datetime

def daily_hr_reminders():
    """
    Send daily HR reminders and notifications
    """
    frappe.logger().info("Running daily HR reminders...")
    
    # Birthday reminders
    send_birthday_reminders()
    
    # Probation ending reminders
    send_probation_reminders()
    
    # Leave balance reminders (quarterly)
    check_and_send_leave_balance_reminders()
    
    # Contract expiry reminders
    send_contract_expiry_reminders()
    
    frappe.logger().info("Daily HR reminders completed")

def weekly_hr_reports():
    """
    Send weekly HR reports
    """
    frappe.logger().info("Running weekly HR reports...")
    
    # Send attendance report
    send_weekly_attendance_report()
    
    # Send leave summary
    send_weekly_leave_summary()
    
    frappe.logger().info("Weekly HR reports completed")

def send_birthday_reminders():
    """
    Send birthday wishes to employees
    """
    try:
        today_date = datetime.now().strftime("%m-%d")
        
        # Find employees with birthday today
        employees = frappe.db.sql("""
            SELECT name, employee_name, company_email, department, designation
            FROM `tabEmployee`
            WHERE status = 'Active'
            AND DATE_FORMAT(date_of_birth, '%%m-%%d') = %s
        """, (today_date,), as_dict=True)
        
        if not employees:
            return
        
        # Send birthday email to each employee
        for emp in employees:
            if emp.company_email:
                try:
                    frappe.sendmail(
                        recipients=emp.company_email,
                        subject=f"🎉 Happy Birthday {emp.employee_name}!",
                        template="Birthday Wishes",
                        args={"doc": emp},
                        now=True
                    )
                except Exception as e:
                    frappe.log_error(f"Failed to send birthday email to {emp.name}: {str(e)}")
        
        # Notify HR about birthdays
        notify_hr_birthdays(employees)
        
    except Exception as e:
        frappe.log_error(f"Error in birthday reminders: {str(e)}")

def notify_hr_birthdays(employees):
    """
    Notify HR about employee birthdays
    """
    try:
        # Get HR Manager emails
        hr_managers = frappe.get_all("Has Role",
            filters={"role": ["in", ["HR Manager", "HR Manager Suite"]]},
            pluck="parent"
        )
        
        if not hr_managers:
            return
        
        # Create notification message
        emp_list = "<ul>"
        for emp in employees:
            emp_list += f"<li><strong>{emp.employee_name}</strong> - {emp.designation} ({emp.department})</li>"
        emp_list += "</ul>"
        
        message = f"""
        <h3>🎂 Birthday Reminder</h3>
        <p>The following employees have birthdays today:</p>
        {emp_list}
        <p>Please ensure they receive birthday wishes and any company benefits.</p>
        """
        
        frappe.sendmail(
            recipients=hr_managers,
            subject=f"Employee Birthdays - {today()}",
            message=message,
            now=True
        )
        
    except Exception as e:
        frappe.log_error(f"Failed to notify HR about birthdays: {str(e)}")

def send_probation_reminders():
    """
    Remind HR about probation ending in next 7 days
    """
    try:
        upcoming_date = add_days(today(), 7)
        
        employees = frappe.get_all("Employee",
            filters={
                "status": "Active",
                "final_confirmation_date": ["between", [today(), upcoming_date]]
            },
            fields=["name", "employee_name", "designation", "department", "final_confirmation_date"]
        )
        
        if not employees:
            return
        
        # Get HR Manager emails
        hr_managers = frappe.get_all("Has Role",
            filters={"role": ["in", ["HR Manager", "HR Manager Suite"]]},
            pluck="parent"
        )
        
        if not hr_managers:
            return
        
        # Create notification message
        emp_list = "<ul>"
        for emp in employees:
            days_left = (getdate(emp.final_confirmation_date) - getdate(today())).days
            emp_list += f"<li><strong>{emp.employee_name}</strong> - {emp.designation} ({emp.department}) - <em>{days_left} days left</em></li>"
        emp_list += "</ul>"
        
        message = f"""
        <h3>⚠️ Probation Completion Reminder</h3>
        <p>The following employees' probation periods are ending soon:</p>
        {emp_list}
        <p>Please complete their performance reviews and confirmation process.</p>
        """
        
        frappe.sendmail(
            recipients=hr_managers,
            subject="Probation Period Ending - Action Required",
            message=message,
            now=True
        )
        
    except Exception as e:
        frappe.log_error(f"Error in probation reminders: {str(e)}")

def check_and_send_leave_balance_reminders():
    """
    Send quarterly leave balance reminders
    """
    try:
        # Check if today is first day of quarter
        today_date = getdate(today())
        if today_date.day != 1 or today_date.month not in [1, 4, 7, 10]:
            return
        
        send_leave_balance_reminders()
        
    except Exception as e:
        frappe.log_error(f"Error in leave balance reminders: {str(e)}")

def send_leave_balance_reminders():
    """
    Send leave balance to all employees
    """
    try:
        employees = frappe.get_all("Employee",
            filters={"status": "Active"},
            fields=["name", "employee_name", "company_email"]
        )
        
        for emp in employees:
            if not emp.company_email:
                continue
            
            # Get leave balance
            leave_balance = get_employee_leave_balance(emp.name)
            
            if not leave_balance:
                continue
            
            # Format leave balance
            balance_html = "<table style='border-collapse: collapse; width: 100%;'>"
            balance_html += "<tr><th style='border: 1px solid #ddd; padding: 8px;'>Leave Type</th><th style='border: 1px solid #ddd; padding: 8px;'>Balance</th></tr>"
            
            for lb in leave_balance:
                balance_html += f"<tr><td style='border: 1px solid #ddd; padding: 8px;'>{lb['leave_type']}</td><td style='border: 1px solid #ddd; padding: 8px;'>{lb['balance']}</td></tr>"
            
            balance_html += "</table>"
            
            message = f"""
            <p>Dear {emp.employee_name},</p>
            <p>Here is your current leave balance:</p>
            {balance_html}
            <p>Please plan your leaves accordingly.</p>
            <p>Best Regards,<br>HR Department</p>
            """
            
            try:
                frappe.sendmail(
                    recipients=emp.company_email,
                    subject="Your Leave Balance Update",
                    message=message
                )
            except Exception as e:
                frappe.log_error(f"Failed to send leave balance to {emp.name}: {str(e)}")
        
    except Exception as e:
        frappe.log_error(f"Error sending leave balance reminders: {str(e)}")

def get_employee_leave_balance(employee):
    """
    Get leave balance for employee
    """
    try:
        leave_types = frappe.get_all("Leave Type", 
            filters={"is_active": 1},
            pluck="name"
        )
        
        balance = []
        for leave_type in leave_types:
            try:
                from erpnext.hr.doctype.leave_application.leave_application import get_leave_balance_on
                bal = get_leave_balance_on(employee, leave_type, today())
                if bal > 0:
                    balance.append({
                        "leave_type": leave_type,
                        "balance": bal
                    })
            except:
                pass
        
        return balance
    except Exception as e:
        frappe.log_error(f"Error getting leave balance for {employee}: {str(e)}")
        return []

def send_contract_expiry_reminders():
    """
    Remind HR about contract expiry
    """
    try:
        expiry_date = add_days(today(), 30)
        
        # Find employees with contracts expiring in 30 days
        employees = frappe.get_all("Employee",
            filters={
                "status": "Active",
                "contract_end_date": ["between", [today(), expiry_date]]
            },
            fields=["name", "employee_name", "designation", "contract_end_date"]
        )
        
        if not employees:
            return
        
        # Get HR Manager emails
        hr_managers = frappe.get_all("Has Role",
            filters={"role": ["in", ["HR Manager", "HR Manager Suite"]]},
            pluck="parent"
        )
        
        if not hr_managers:
            return
        
        # Create notification
        emp_list = "<ul>"
        for emp in employees:
            days_left = (getdate(emp.contract_end_date) - getdate(today())).days
            emp_list += f"<li><strong>{emp.employee_name}</strong> - {emp.designation} - Contract ends on {emp.contract_end_date} ({days_left} days)</li>"
        emp_list += "</ul>"
        
        message = f"""
        <h3>⚠️ Contract Expiry Reminder</h3>
        <p>The following employees' contracts are expiring soon:</p>
        {emp_list}
        <p>Please take necessary action for renewal or separation.</p>
        """
        
        frappe.sendmail(
            recipients=hr_managers,
            subject="Contract Expiry - Action Required",
            message=message
        )
        
    except Exception as e:
        frappe.log_error(f"Error in contract expiry reminders: {str(e)}")

def send_weekly_attendance_report():
    """
    Send weekly attendance summary to HR
    """
    # Implementation for weekly attendance report
    pass

def send_weekly_leave_summary():
    """
    Send weekly leave summary to HR
    """
    # Implementation for weekly leave summary
    pass