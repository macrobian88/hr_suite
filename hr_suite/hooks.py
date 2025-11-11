from . import __version__ as app_version

app_name = "hr_suite"
app_title = "HR Suite"
app_publisher = "Your Company"
app_description = "Complete HR Management Solution with ERPNext - One Click Setup"
app_email = "support@yourcompany.com"
app_license = "MIT"
app_version = app_version

# Required apps - ERPNext includes HR module
required_apps = ["erpnext"]

# Fixtures - Data that will be installed automatically
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [["module", "in", ["HR Suite"]]]
    },
    {
        "doctype": "Role",
        "filters": [["name", "in", ["HR Manager Suite", "HR User Suite", "Employee Self Service"]]]
    }
]

# After install hook
after_install = "hr_suite.install.after_install"

# Scheduled tasks
scheduler_events = {
    "daily": [
        "hr_suite.tasks.daily_hr_reminders"
    ],
    "weekly": [
        "hr_suite.tasks.weekly_hr_reports"
    ]
}

# Document events
doc_events = {
    "Employee": {
        "after_insert": "hr_suite.api.employee.after_employee_insert"
    },
    "Leave Application": {
        "on_submit": "hr_suite.api.leave.on_leave_submit"
    }
}

# Website route rules
website_route_rules = [
    {"from_route": "/hr-portal", "to_route": "HR Portal"},
    {"from_route": "/hr-dashboard", "to_route": "HR Dashboard"}
]

# Permission query conditions
permission_query_conditions = {
    "Employee": "hr_suite.permissions.employee_query"
}

# Has permission
has_permission = {
    "Employee": "hr_suite.permissions.has_employee_permission"
}

# Whitelisted methods for API
whitelisted = [
    "hr_suite.api.dashboard.get_hr_stats",
    "hr_suite.api.employee.get_employee_details",
    "hr_suite.setup_wizard.get_setup_progress"
]

# On logout
on_logout = "hr_suite.api.auth.clear_employee_cache"