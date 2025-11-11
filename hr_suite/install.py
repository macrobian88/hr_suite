import frappe
from frappe import _
from frappe.utils import today, add_days, add_months
import subprocess
import os

def before_install():
    """
    Check and install required dependencies before HR Suite installation
    """
    frappe.msgprint(_("Checking dependencies..."), alert=True)
    
    # Check if we're on Frappe Cloud or self-hosted
    is_cloud = is_frappe_cloud()
    
    if is_cloud:
        # On Frappe Cloud, just verify - can't auto-install
        verify_dependencies_cloud()
    else:
        # On self-hosted, auto-install if needed
        install_dependencies_self_hosted()

def is_frappe_cloud():
    """
    Detect if running on Frappe Cloud
    """
    # Check for Frappe Cloud environment indicators
    site_config = frappe.get_site_config()
    return site_config.get('is_frappe_cloud') or os.path.exists('/home/frappe/frappe-cloud')

def verify_dependencies_cloud():
    """
    Verify dependencies on Frappe Cloud
    Can't auto-install, but provide helpful messages
    """
    installed_apps = frappe.get_installed_apps()
    missing_apps = []
    
    if "erpnext" not in installed_apps:
        missing_apps.append("ERPNext")
    
    if "hrms" not in installed_apps:
        missing_apps.append("HRMS")
    
    if missing_apps:
        message = f"""
        <h3>Missing Required Apps</h3>
        <p>HR Suite requires the following apps to be installed on your site:</p>
        <ul>
            {''.join([f'<li>{app}</li>' for app in missing_apps])}
        </ul>
        <p><strong>On Frappe Cloud, please:</strong></p>
        <ol>
            <li>Go to your Site → Apps tab</li>
            <li>Install {' and '.join(missing_apps)}</li>
            <li>Then install HR Suite</li>
        </ol>
        """
        frappe.throw(message, title="Dependencies Required")
    
    frappe.msgprint(_("All dependencies verified! ✅"), alert=True, indicator="green")

def install_dependencies_self_hosted():
    """
    Auto-install ERPNext and HRMS on self-hosted installations
    """
    try:
        installed_apps = frappe.get_installed_apps()
        bench_path = frappe.utils.get_bench_path()
        site_name = frappe.local.site
        
        # Check and install ERPNext
        if "erpnext" not in installed_apps:
            frappe.msgprint(_("ERPNext not found. Installing ERPNext..."), alert=True)
            
            # Check if ERPNext is in bench apps
            bench_apps = get_bench_apps()
            
            if "erpnext" not in bench_apps:
                # Get ERPNext app
                frappe.msgprint(_("Downloading ERPNext..."), alert=True)
                run_command(f"cd {bench_path} && bench get-app erpnext --branch version-15")
            
            # Install to site
            frappe.msgprint(_("Installing ERPNext to site..."), alert=True)
            run_command(f"cd {bench_path} && bench --site {site_name} install-app erpnext")
            frappe.msgprint(_("ERPNext installed successfully! ✅"), alert=True, indicator="green")
        else:
            frappe.msgprint(_("ERPNext already installed ✅"), alert=True, indicator="green")
        
        # Check and install HRMS
        if "hrms" not in installed_apps:
            frappe.msgprint(_("HRMS not found. Installing HRMS..."), alert=True)
            
            # Check if HRMS is in bench apps
            bench_apps = get_bench_apps()
            
            if "hrms" not in bench_apps:
                # Get HRMS app
                frappe.msgprint(_("Downloading HRMS..."), alert=True)
                run_command(f"cd {bench_path} && bench get-app hrms --branch version-15")
            
            # Install to site
            frappe.msgprint(_("Installing HRMS to site..."), alert=True)
            run_command(f"cd {bench_path} && bench --site {site_name} install-app hrms")
            frappe.msgprint(_("HRMS installed successfully! ✅"), alert=True, indicator="green")
        else:
            frappe.msgprint(_("HRMS already installed ✅"), alert=True, indicator="green")
        
        frappe.msgprint(_("All dependencies are ready! Proceeding with HR Suite installation..."), alert=True, indicator="green")
        
    except Exception as e:
        frappe.log_error(f"Error installing dependencies: {str(e)}")
        error_msg = f"""
        <h3>Could not auto-install dependencies</h3>
        <p>Please install manually:</p>
        <pre>
cd {bench_path}
bench get-app erpnext --branch version-15
bench get-app hrms --branch version-15
bench --site {site_name} install-app erpnext
bench --site {site_name} install-app hrms
bench --site {site_name} install-app hr_suite
        </pre>
        <p><strong>Error:</strong> {str(e)}</p>
        """
        frappe.throw(error_msg, title="Manual Installation Required")

def get_bench_apps():
    """
    Get list of apps available in the bench
    """
    try:
        bench_path = frappe.utils.get_bench_path()
        apps_txt_path = os.path.join(bench_path, "sites", "apps.txt")
        
        if os.path.exists(apps_txt_path):
            with open(apps_txt_path, 'r') as f:
                return [app.strip() for app in f.readlines()]
        return []
    except Exception as e:
        frappe.log_error(f"Error getting bench apps: {str(e)}")
        return []

def run_command(command):
    """
    Run shell command
    """
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        frappe.log_error(f"Command failed: {command}\nError: {e.stderr}")
        raise Exception(f"Command failed: {e.stderr}")

def after_install():
    """
    Main installation function that sets up everything
    """
    frappe.msgprint(_("Setting up HR Suite..."), alert=True)
    
    # Step 1: Create default HR roles
    create_hr_roles()
    
    # Step 2: Setup HR configurations
    setup_hr_settings()
    
    # Step 3: Create default departments
    create_default_departments()
    
    # Step 4: Create default designations
    create_default_designations()
    
    # Step 5: Setup leave types
    setup_leave_types()
    
    # Step 6: Setup attendance settings
    setup_attendance_settings()
    
    # Step 7: Setup payroll settings
    setup_payroll_settings()
    
    # Step 8: Create sample workflows
    create_hr_workflows()
    
    # Step 9: Setup email templates
    setup_email_templates()
    
    # Step 10: Create dashboard
    create_hr_dashboard()
    
    frappe.db.commit()
    frappe.msgprint(_("HR Suite installed successfully! 🎉"), alert=True, indicator="green")

def create_hr_roles():
    """Create custom HR roles"""
    roles = [
        {
            "role_name": "HR Manager Suite",
            "desk_access": 1,
            "is_custom": 1
        },
        {
            "role_name": "HR User Suite",
            "desk_access": 1,
            "is_custom": 1
        },
        {
            "role_name": "Employee Self Service",
            "desk_access": 1,
            "is_custom": 1
        }
    ]
    
    for role in roles:
        if not frappe.db.exists("Role", role["role_name"]):
            doc = frappe.get_doc({
                "doctype": "Role",
                "role_name": role["role_name"],
                "desk_access": role["desk_access"],
                "is_custom": role["is_custom"]
            })
            doc.insert(ignore_permissions=True)

def setup_hr_settings():
    """Configure HR Settings with defaults"""
    try:
        hr_settings = frappe.get_doc("HR Settings")
        
        # Basic settings
        hr_settings.emp_created_by = "Naming Series"
        hr_settings.stop_birthday_reminders = 0
        hr_settings.send_holiday_reminders = 1
        hr_settings.auto_leave_encashment = 0
        
        # Leave settings
        hr_settings.leave_approver_mandatory_in_leave_application = 1
        hr_settings.show_leaves_of_all_department_members_in_calendar = 1
        hr_settings.restrict_backdated_leave_application = 1
        hr_settings.carry_forward_all_leaves = 0
        
        # Payroll settings
        hr_settings.include_holidays_in_total_working_days = 0
        hr_settings.payroll_based_on = "Attendance"
        hr_settings.consider_unmarked_attendance_as = "Absent"
        
        # Email settings
        hr_settings.send_leave_notification = 1
        hr_settings.email_salary_slip_to_employee = 1
        
        hr_settings.save(ignore_permissions=True)
        frappe.msgprint(_("HR Settings configured"), alert=True)
        
    except Exception as e:
        frappe.log_error(f"Error in HR Settings: {str(e)}")

def create_default_departments():
    """Create default departments"""
    departments = [
        "Human Resources",
        "Operations",
        "Finance",
        "Sales",
        "Marketing",
        "IT",
        "Administration",
        "Customer Support"
    ]
    
    for dept in departments:
        if not frappe.db.exists("Department", dept):
            doc = frappe.get_doc({
                "doctype": "Department",
                "department_name": dept,
                "is_group": 0
            })
            doc.insert(ignore_permissions=True)
    
    frappe.msgprint(_("Default departments created"), alert=True)

def create_default_designations():
    """Create default designations"""
    designations = [
        "CEO",
        "Manager",
        "Senior Developer",
        "Developer",
        "HR Manager",
        "HR Executive",
        "Sales Manager",
        "Sales Executive",
        "Marketing Manager",
        "Marketing Executive",
        "Accountant",
        "Admin"
    ]
    
    for designation in designations:
        if not frappe.db.exists("Designation", designation):
            doc = frappe.get_doc({
                "doctype": "Designation",
                "designation_name": designation
            })
            doc.insert(ignore_permissions=True)
    
    frappe.msgprint(_("Default designations created"), alert=True)

def setup_leave_types():
    """Create default leave types"""
    leave_types = [
        {
            "leave_type_name": "Annual Leave",
            "max_leaves_allowed": 21,
            "is_carry_forward": 1,
            "max_continuous_days_allowed": 15,
            "applicable_after": 90,
            "allow_negative": 0,
            "include_holiday": 0,
            "is_lwp": 0
        },
        {
            "leave_type_name": "Sick Leave",
            "max_leaves_allowed": 12,
            "is_carry_forward": 0,
            "applicable_after": 0,
            "allow_negative": 0,
            "include_holiday": 1,
            "is_lwp": 0
        },
        {
            "leave_type_name": "Casual Leave",
            "max_leaves_allowed": 7,
            "is_carry_forward": 0,
            "applicable_after": 0,
            "allow_negative": 0,
            "include_holiday": 0,
            "is_lwp": 0
        },
        {
            "leave_type_name": "Leave Without Pay",
            "max_leaves_allowed": 0,
            "is_carry_forward": 0,
            "applicable_after": 0,
            "allow_negative": 1,
            "include_holiday": 1,
            "is_lwp": 1
        },
        {
            "leave_type_name": "Maternity Leave",
            "max_leaves_allowed": 90,
            "is_carry_forward": 0,
            "applicable_after": 180,
            "allow_negative": 0,
            "include_holiday": 1,
            "is_lwp": 0
        },
        {
            "leave_type_name": "Paternity Leave",
            "max_leaves_allowed": 5,
            "is_carry_forward": 0,
            "applicable_after": 180,
            "allow_negative": 0,
            "include_holiday": 1,
            "is_lwp": 0
        }
    ]
    
    for leave in leave_types:
        if not frappe.db.exists("Leave Type", leave["leave_type_name"]):
            doc = frappe.get_doc({
                "doctype": "Leave Type",
                **leave
            })
            doc.insert(ignore_permissions=True)
    
    frappe.msgprint(_("Leave types configured"), alert=True)

def setup_attendance_settings():
    """Setup attendance configuration"""
    try:
        # Create default shift
        if not frappe.db.exists("Shift Type", "General Shift"):
            shift = frappe.get_doc({
                "doctype": "Shift Type",
                "name": "General Shift",
                "start_time": "09:00:00",
                "end_time": "18:00:00",
                "enable_auto_attendance": 1,
                "determine_check_in_and_check_out": "Alternating entries as IN and OUT during the same shift",
                "working_hours_threshold_for_half_day": 4,
                "working_hours_threshold_for_absent": 0
            })
            shift.insert(ignore_permissions=True)
        
        frappe.msgprint(_("Attendance settings configured"), alert=True)
        
    except Exception as e:
        frappe.log_error(f"Error in Attendance Settings: {str(e)}")

def setup_payroll_settings():
    """Setup payroll configuration"""
    try:
        if not frappe.db.exists("Payroll Settings"):
            return
            
        payroll_settings = frappe.get_doc("Payroll Settings")
        payroll_settings.email_salary_slip_to_employee = 1
        payroll_settings.encrypt_salary_slips_in_emails = 1
        payroll_settings.include_holidays_in_total_working_days = 0
        payroll_settings.save(ignore_permissions=True)
        
        # Create default salary components
        create_salary_components()
        
        frappe.msgprint(_("Payroll settings configured"), alert=True)
        
    except Exception as e:
        frappe.log_error(f"Error in Payroll Settings: {str(e)}")

def create_salary_components():
    """Create basic salary components"""
    components = [
        {
            "salary_component": "Basic Salary",
            "type": "Earning",
            "is_tax_applicable": 1
        },
        {
            "salary_component": "Housing Allowance",
            "type": "Earning",
            "is_tax_applicable": 1
        },
        {
            "salary_component": "Transport Allowance",
            "type": "Earning",
            "is_tax_applicable": 1
        },
        {
            "salary_component": "Medical Allowance",
            "type": "Earning",
            "is_tax_applicable": 0
        },
        {
            "salary_component": "Income Tax",
            "type": "Deduction",
            "is_tax_applicable": 0
        },
        {
            "salary_component": "Professional Tax",
            "type": "Deduction",
            "is_tax_applicable": 0
        }
    ]
    
    for component in components:
        if not frappe.db.exists("Salary Component", component["salary_component"]):
            doc = frappe.get_doc({
                "doctype": "Salary Component",
                **component
            })
            doc.insert(ignore_permissions=True)

def create_hr_workflows():
    """Create approval workflows for HR processes"""
    # Workflows are complex, can be created manually or use fixtures
    frappe.msgprint(_("HR workflows ready for configuration"), alert=True)

def setup_email_templates():
    """Create email templates for HR processes"""
    templates = [
        {
            "name": "Leave Approval Notification",
            "subject": "Leave Application Approved",
            "response": """
            <p>Dear {{ doc.employee_name }},</p>
            <p>Your leave application from {{ doc.from_date }} to {{ doc.to_date }} has been approved.</p>
            <p>Leave Type: {{ doc.leave_type }}</p>
            <p>Best Regards,<br>HR Department</p>
            """
        },
        {
            "name": "Welcome Email",
            "subject": "Welcome to {{ frappe.defaults.get_defaults().company }}",
            "response": """
            <p>Dear {{ doc.employee_name }},</p>
            <p>Welcome to our organization! We are excited to have you on board.</p>
            <p>Your employee ID is: {{ doc.name }}</p>
            <p>Best Regards,<br>HR Department</p>
            """
        }
    ]
    
    for template in templates:
        if not frappe.db.exists("Email Template", template["name"]):
            doc = frappe.get_doc({
                "doctype": "Email Template",
                **template
            })
            doc.insert(ignore_permissions=True)
    
    frappe.msgprint(_("Email templates created"), alert=True)

def create_hr_dashboard():
    """Create HR Dashboard"""
    try:
        dashboard_name = "HR Suite Dashboard"
        
        if not frappe.db.exists("Dashboard", dashboard_name):
            dashboard = frappe.get_doc({
                "doctype": "Dashboard",
                "dashboard_name": dashboard_name,
                "module": "HR",
                "is_default": 1
            })
            dashboard.insert(ignore_permissions=True)
        
        frappe.msgprint(_("HR Dashboard created"), alert=True)
        
    except Exception as e:
        frappe.log_error(f"Error creating dashboard: {str(e)}")