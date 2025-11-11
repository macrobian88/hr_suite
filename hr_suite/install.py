import frappe
from frappe import _
import subprocess
import os

def before_install():
    """
    Check dependencies before HR Suite installation
    On Frappe Cloud: Just verify and show instructions if missing
    On Self-Hosted: Auto-install if missing
    """
    # Check if we're on Frappe Cloud
    if is_frappe_cloud():
        verify_dependencies_cloud()
    else:
        install_dependencies_self_hosted()

def is_frappe_cloud():
    """
    Detect if running on Frappe Cloud
    Multiple detection methods for reliability
    """
    # Method 1: Check site name
    try:
        site = frappe.local.site
        if site and ('frappe.cloud' in site or '.frappecloud.com' in site):
            return True
    except:
        pass
    
    # Method 2: Check site config
    try:
        site_config = frappe.get_site_config()
        if site_config.get('is_frappe_cloud'):
            return True
    except:
        pass
    
    # Method 3: Check environment
    if os.environ.get('FRAPPE_CLOUD') or os.environ.get('FC_SITE'):
        return True
    
    # Method 4: Check for Frappe Cloud directory structure
    if os.path.exists('/home/frappe/frappe-cloud'):
        return True
    
    # Method 5: Check bench path (Frappe Cloud uses specific path)
    bench_path = os.getcwd()
    if '/home/frappe/frappe-bench' in bench_path and os.path.exists('/workspace'):
        return True
    
    return False

def verify_dependencies_cloud():
    """
    Verify dependencies on Frappe Cloud
    Show simple, clear instructions if missing
    """
    installed_apps = frappe.get_installed_apps()
    missing = []
    
    if "erpnext" not in installed_apps:
        missing.append("ERPNext")
    if "hrms" not in installed_apps:
        missing.append("HRMS")
    
    if missing:
        # Create simple error message that won't cause database issues
        apps_list = " and ".join(missing)
        message = f"HR Suite requires {apps_list} to be installed first. Please install {apps_list} on your site, then install HR Suite."
        frappe.throw(message, title="Missing Dependencies")

def install_dependencies_self_hosted():
    """
    Auto-install ERPNext and HRMS on self-hosted
    """
    try:
        installed_apps = frappe.get_installed_apps()
        bench_path = get_bench_path()
        site_name = frappe.local.site
        
        # Install ERPNext if missing
        if "erpnext" not in installed_apps:
            print("Installing ERPNext...")
            
            bench_apps = get_bench_apps()
            if "erpnext" not in bench_apps:
                run_command(f"cd {bench_path} && bench get-app erpnext --branch version-15")
            
            run_command(f"cd {bench_path} && bench --site {site_name} install-app erpnext")
            print("ERPNext installed successfully!")
        
        # Refresh installed apps
        installed_apps = frappe.get_installed_apps()
        
        # Install HRMS if missing
        if "hrms" not in installed_apps:
            print("Installing HRMS...")
            
            bench_apps = get_bench_apps()
            if "hrms" not in bench_apps:
                run_command(f"cd {bench_path} && bench get-app hrms --branch version-15")
            
            run_command(f"cd {bench_path} && bench --site {site_name} install-app hrms")
            print("HRMS installed successfully!")
        
    except Exception as e:
        error_msg = f"Auto-install failed. Please install manually: bench get-app erpnext && bench get-app hrms && bench install-app erpnext && bench install-app hrms. Error: {str(e)[:100]}"
        frappe.throw(error_msg, title="Manual Installation Required")

def get_bench_path():
    """Get bench path"""
    try:
        return frappe.utils.get_bench_path()
    except:
        return os.getcwd()

def get_bench_apps():
    """Get list of apps in bench"""
    try:
        bench_path = get_bench_path()
        apps_txt = os.path.join(bench_path, "sites", "apps.txt")
        if os.path.exists(apps_txt):
            with open(apps_txt, 'r') as f:
                return [app.strip() for app in f.readlines()]
    except:
        pass
    return []

def run_command(command):
    """Run shell command"""
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True, timeout=300)
    return result.stdout

def after_install():
    """
    Configure HR Suite after installation
    """
    print("Configuring HR Suite...")
    
    create_hr_roles()
    setup_hr_settings()
    create_default_departments()
    create_default_designations()
    setup_leave_types()
    setup_attendance_settings()
    setup_payroll_settings()
    setup_email_templates()
    create_hr_dashboard()
    
    frappe.db.commit()
    print("HR Suite configured successfully!")

def create_hr_roles():
    """Create HR roles"""
    roles = [
        {"role_name": "HR Manager Suite", "desk_access": 1, "is_custom": 1},
        {"role_name": "HR User Suite", "desk_access": 1, "is_custom": 1},
        {"role_name": "Employee Self Service", "desk_access": 1, "is_custom": 1}
    ]
    
    for role in roles:
        if not frappe.db.exists("Role", role["role_name"]):
            frappe.get_doc({"doctype": "Role", **role}).insert(ignore_permissions=True)

def setup_hr_settings():
    """Configure HR Settings"""
    try:
        hr_settings = frappe.get_doc("HR Settings")
        hr_settings.emp_created_by = "Naming Series"
        hr_settings.stop_birthday_reminders = 0
        hr_settings.send_holiday_reminders = 1
        hr_settings.leave_approver_mandatory_in_leave_application = 1
        hr_settings.payroll_based_on = "Attendance"
        hr_settings.send_leave_notification = 1
        hr_settings.email_salary_slip_to_employee = 1
        hr_settings.save(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"HR Settings error: {str(e)}")

def create_default_departments():
    """Create default departments"""
    departments = ["Human Resources", "Operations", "Finance", "Sales", "Marketing", "IT", "Administration", "Customer Support"]
    
    for dept in departments:
        if not frappe.db.exists("Department", dept):
            frappe.get_doc({"doctype": "Department", "department_name": dept, "is_group": 0}).insert(ignore_permissions=True)

def create_default_designations():
    """Create default designations"""
    designations = ["CEO", "Manager", "Senior Developer", "Developer", "HR Manager", "HR Executive", "Sales Manager", "Sales Executive", "Marketing Manager", "Marketing Executive", "Accountant", "Admin"]
    
    for designation in designations:
        if not frappe.db.exists("Designation", designation):
            frappe.get_doc({"doctype": "Designation", "designation_name": designation}).insert(ignore_permissions=True)

def setup_leave_types():
    """Create leave types"""
    leave_types = [
        {"leave_type_name": "Annual Leave", "max_leaves_allowed": 21, "is_carry_forward": 1, "applicable_after": 90},
        {"leave_type_name": "Sick Leave", "max_leaves_allowed": 12, "is_carry_forward": 0, "applicable_after": 0},
        {"leave_type_name": "Casual Leave", "max_leaves_allowed": 7, "is_carry_forward": 0, "applicable_after": 0},
        {"leave_type_name": "Leave Without Pay", "max_leaves_allowed": 0, "is_carry_forward": 0, "is_lwp": 1},
        {"leave_type_name": "Maternity Leave", "max_leaves_allowed": 90, "is_carry_forward": 0, "applicable_after": 180},
        {"leave_type_name": "Paternity Leave", "max_leaves_allowed": 5, "is_carry_forward": 0, "applicable_after": 180}
    ]
    
    for leave in leave_types:
        if not frappe.db.exists("Leave Type", leave["leave_type_name"]):
            frappe.get_doc({"doctype": "Leave Type", **leave}).insert(ignore_permissions=True)

def setup_attendance_settings():
    """Setup attendance"""
    try:
        if not frappe.db.exists("Shift Type", "General Shift"):
            frappe.get_doc({
                "doctype": "Shift Type",
                "name": "General Shift",
                "start_time": "09:00:00",
                "end_time": "18:00:00",
                "enable_auto_attendance": 1
            }).insert(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"Attendance settings error: {str(e)}")

def setup_payroll_settings():
    """Setup payroll"""
    try:
        components = [
            {"salary_component": "Basic Salary", "type": "Earning", "is_tax_applicable": 1},
            {"salary_component": "Housing Allowance", "type": "Earning", "is_tax_applicable": 1},
            {"salary_component": "Transport Allowance", "type": "Earning", "is_tax_applicable": 1},
            {"salary_component": "Medical Allowance", "type": "Earning", "is_tax_applicable": 0},
            {"salary_component": "Income Tax", "type": "Deduction", "is_tax_applicable": 0},
            {"salary_component": "Professional Tax", "type": "Deduction", "is_tax_applicable": 0}
        ]
        
        for component in components:
            if not frappe.db.exists("Salary Component", component["salary_component"]):
                frappe.get_doc({"doctype": "Salary Component", **component}).insert(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"Payroll settings error: {str(e)}")

def setup_email_templates():
    """Create email templates"""
    templates = [
        {"name": "Leave Approval Notification", "subject": "Leave Application Approved", "response": "<p>Dear {{ doc.employee_name }},</p><p>Your leave application has been approved.</p>"},
        {"name": "Welcome Email", "subject": "Welcome to the Team", "response": "<p>Dear {{ doc.employee_name }},</p><p>Welcome to our organization!</p>"}
    ]
    
    for template in templates:
        if not frappe.db.exists("Email Template", template["name"]):
            frappe.get_doc({"doctype": "Email Template", **template}).insert(ignore_permissions=True)

def create_hr_dashboard():
    """Create HR dashboard"""
    try:
        if not frappe.db.exists("Dashboard", "HR Suite Dashboard"):
            frappe.get_doc({"doctype": "Dashboard", "dashboard_name": "HR Suite Dashboard", "module": "HR"}).insert(ignore_permissions=True)
    except Exception as e:
        frappe.log_error(f"Dashboard error: {str(e)}")