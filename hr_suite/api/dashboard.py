import frappe
from frappe import _
from frappe.utils import today, add_days, get_first_day, get_last_day, getdate
from datetime import datetime, timedelta

@frappe.whitelist()
def get_hr_stats():
    """
    Get HR statistics for dashboard
    """
    if not frappe.has_permission("Employee", "read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    stats = {
        "total_employees": get_total_employees(),
        "active_employees": get_active_employees(),
        "on_leave_today": get_on_leave_count(),
        "present_today": get_present_count(),
        "pending_leave_applications": get_pending_leaves(),
        "new_joinings_this_month": get_new_joinings(),
        "upcoming_birthdays": get_upcoming_birthdays(),
        "probation_ending": get_probation_ending(),
        "department_wise_count": get_department_wise_count(),
        "leave_type_usage": get_leave_type_usage(),
        "attendance_summary": get_attendance_summary()
    }
    
    return stats

def get_total_employees():
    """Get total number of employees"""
    return frappe.db.count("Employee")

def get_active_employees():
    """Get active employees count"""
    return frappe.db.count("Employee", {"status": "Active"})

def get_on_leave_count():
    """Get employees on leave today"""
    return frappe.db.count("Leave Application", {
        "status": "Approved",
        "docstatus": 1,
        "from_date": ["<=", today()],
        "to_date": [">=", today()]
    })

def get_present_count():
    """Get employees present today"""
    return frappe.db.count("Attendance", {
        "attendance_date": today(),
        "status": "Present"
    })

def get_pending_leaves():
    """Get pending leave applications count"""
    return frappe.db.count("Leave Application", {
        "status": "Open",
        "docstatus": 0
    })

def get_new_joinings():
    """Get new joinings this month"""
    first_day = get_first_day(today())
    last_day = get_last_day(today())
    
    new_joinings = frappe.db.count("Employee", {
        "status": "Active",
        "date_of_joining": ["between", [first_day, last_day]]
    })
    
    # Get list of new employees
    employees = frappe.get_all("Employee",
        filters={
            "status": "Active",
            "date_of_joining": ["between", [first_day, last_day]]
        },
        fields=["name", "employee_name", "designation", "date_of_joining"],
        order_by="date_of_joining desc"
    )
    
    return {
        "count": new_joinings,
        "employees": employees
    }

def get_upcoming_birthdays(days=7):
    """Get upcoming birthdays in next N days"""
    today_date = datetime.now()
    
    employees = frappe.get_all("Employee",
        filters={"status": "Active"},
        fields=["name", "employee_name", "date_of_birth", "department"]
    )
    
    upcoming = []
    for emp in employees:
        if emp.date_of_birth:
            # Get this year's birthday
            birth_date = getdate(emp.date_of_birth)
            this_year_birthday = birth_date.replace(year=today_date.year)
            
            # If birthday has passed this year, check next year
            if this_year_birthday < today_date.date():
                this_year_birthday = birth_date.replace(year=today_date.year + 1)
            
            days_until = (this_year_birthday - today_date.date()).days
            
            if 0 <= days_until <= days:
                upcoming.append({
                    "employee": emp.name,
                    "employee_name": emp.employee_name,
                    "department": emp.department,
                    "date_of_birth": emp.date_of_birth,
                    "birthday_date": this_year_birthday,
                    "days_until": days_until
                })
    
    # Sort by days until birthday
    upcoming.sort(key=lambda x: x["days_until"])
    
    return upcoming

def get_probation_ending(days=30):
    """Get employees whose probation is ending soon"""
    end_date = add_days(today(), days)
    
    employees = frappe.get_all("Employee",
        filters={
            "status": "Active",
            "final_confirmation_date": ["between", [today(), end_date]]
        },
        fields=["name", "employee_name", "designation", "department", "final_confirmation_date"],
        order_by="final_confirmation_date asc"
    )
    
    # Calculate days until confirmation
    for emp in employees:
        if emp.final_confirmation_date:
            days_until = (getdate(emp.final_confirmation_date) - getdate(today())).days
            emp["days_until"] = days_until
    
    return employees

def get_department_wise_count():
    """Get employee count by department"""
    departments = frappe.db.sql("""
        SELECT 
            department,
            COUNT(*) as count
        FROM `tabEmployee`
        WHERE status = 'Active'
        GROUP BY department
        ORDER BY count DESC
    """, as_dict=True)
    
    return departments

def get_leave_type_usage():
    """Get leave type usage statistics"""
    first_day = get_first_day(today())
    last_day = get_last_day(today())
    
    leave_usage = frappe.db.sql("""
        SELECT 
            leave_type,
            COUNT(*) as applications,
            SUM(total_leave_days) as total_days
        FROM `tabLeave Application`
        WHERE status = 'Approved'
        AND docstatus = 1
        AND from_date >= %s
        AND to_date <= %s
        GROUP BY leave_type
        ORDER BY total_days DESC
    """, (first_day, last_day), as_dict=True)
    
    return leave_usage

def get_attendance_summary(days=30):
    """Get attendance summary for last N days"""
    from_date = add_days(today(), -days)
    
    summary = frappe.db.sql("""
        SELECT 
            status,
            COUNT(*) as count
        FROM `tabAttendance`
        WHERE attendance_date >= %s
        AND attendance_date <= %s
        GROUP BY status
    """, (from_date, today()), as_dict=True)
    
    return summary

@frappe.whitelist()
def get_employee_leave_balance(employee):
    """Get leave balance for specific employee"""
    if not frappe.has_permission("Employee", "read"):
        frappe.throw(_("Not permitted"), frappe.PermissionError)
    
    leave_types = frappe.get_all("Leave Type", 
        filters={"is_active": 1},
        fields=["name", "leave_type_name"]
    )
    
    balance = []
    for lt in leave_types:
        try:
            from erpnext.hr.doctype.leave_application.leave_application import get_leave_balance_on
            bal = get_leave_balance_on(employee, lt.name, today())
            balance.append({
                "leave_type": lt.name,
                "leave_type_name": lt.leave_type_name,
                "balance": bal
            })
        except:
            balance.append({
                "leave_type": lt.name,
                "leave_type_name": lt.leave_type_name,
                "balance": 0
            })
    
    return balance