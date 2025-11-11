import frappe
from frappe.utils import today, get_first_day, get_last_day

@frappe.whitelist()
def get_hr_stats():
    """Get HR statistics for dashboard"""
    
    stats = {
        "total_employees": frappe.db.count("Employee", {"status": "Active"}),
        "on_leave_today": get_on_leave_count(),
        "pending_leave_applications": frappe.db.count("Leave Application", 
            {"status": "Open", "docstatus": 0}),
        "new_joinings_this_month": get_new_joinings(),
        "upcoming_birthdays": get_upcoming_birthdays(),
        "probation_ending": get_probation_ending()
    }
    
    return stats

def get_on_leave_count():
    """Get employees on leave today"""
    return frappe.db.count("Leave Application", {
        "status": "Approved",
        "from_date": ["<=", today()],
        "to_date": [">=", today()]
    })

def get_new_joinings():
    """Get new joinings this month"""
    return frappe.db.count("Employee", {
        "status": "Active",
        "date_of_joining": ["between", [get_first_day(today()), get_last_day(today())]]
    })

def get_upcoming_birthdays():
    """Get upcoming birthdays in next 7 days"""
    # Implementation
    return []

def get_probation_ending():
    """Get employees whose probation is ending soon"""
    # Implementation
    return []