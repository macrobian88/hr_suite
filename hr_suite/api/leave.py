import frappe
from frappe import _

def on_leave_submit(doc, method):
    """
    Triggered when leave application is submitted
    """
    # Send notification to leave approver
    send_leave_notification(doc)
    
    # Update leave balance
    update_leave_balance(doc)

def send_leave_notification(leave_app):
    """
    Send leave application notification to approver
    """
    if not leave_app.leave_approver:
        return
    
    try:
        message = f"""
        <p>A new leave application requires your approval.</p>
        <p><strong>Employee:</strong> {leave_app.employee_name}</p>
        <p><strong>Leave Type:</strong> {leave_app.leave_type}</p>
        <p><strong>From:</strong> {leave_app.from_date} <strong>To:</strong> {leave_app.to_date}</p>
        <p><strong>Total Days:</strong> {leave_app.total_leave_days}</p>
        <p><strong>Reason:</strong> {leave_app.description or 'Not specified'}</p>
        """
        
        frappe.sendmail(
            recipients=leave_app.leave_approver,
            subject=f"Leave Approval Required - {leave_app.employee_name}",
            message=message,
            reference_doctype="Leave Application",
            reference_name=leave_app.name
        )
    except Exception as e:
        frappe.log_error(f"Failed to send leave notification: {str(e)}")

def update_leave_balance(leave_app):
    """
    Update leave balance after approval/rejection
    """
    # This is handled automatically by ERPNext
    pass