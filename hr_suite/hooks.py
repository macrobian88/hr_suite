from . import __version__ as app_version

app_name = "hr_suite"
app_title = "HR Suite"
app_publisher = "Your Company"
app_description = "Complete HR Management Solution with ERPNext"
app_email = "support@yourcompany.com"
app_license = "MIT"
app_version = "1.0.0"

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
        "filters": [["name", "in", ["HR Manager Suite", "HR User Suite"]]]
    }
]

# After install hook
after_install = "hr_suite.install.after_install"

# Scheduled tasks
scheduler_events = {
    "daily": [
        "hr_suite.tasks.daily_hr_reminders"
    ]
}

# Whitelisted methods
doc_events = {
    "Employee": {
        "after_insert": "hr_suite.api.employee.after_employee_insert"
    }
}

# Website settings
website_route_rules = [
    {"from_route": "/hr-portal", "to_route": "HR Portal"}
]
