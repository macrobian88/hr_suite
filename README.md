# HR Suite - Complete HR Management Solution

<div align="center">
  <img src="https://img.shields.io/badge/Frappe-Framework-blue" alt="Frappe">
  <img src="https://img.shields.io/badge/ERPNext-Compatible-green" alt="ERPNext">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
  <img src="https://img.shields.io/badge/Version-1.0.0-red" alt="Version">
</div>

## 🎯 Overview

**HR Suite** is a comprehensive HR management solution that provides **one-click installation and configuration** for ERPNext's HR module. It automates the entire setup process, creating all necessary configurations, departments, designations, leave types, and workflows out of the box.

Perfect for HR firms and companies looking to implement a complete HR management system without manual configuration!

## ✨ Features

### 🚀 One-Click Installation
- Automated installation and configuration
- Pre-configured HR settings
- Ready-to-use out of the box

### 👥 Employee Management
- Auto-create user accounts for new employees
- Automated welcome email notifications
- Automatic leave allocation on joining
- Employee self-service portal

### 🏢 Pre-Configured Setup
- **8 Default Departments**: HR, Operations, Finance, Sales, Marketing, IT, Administration, Customer Support
- **12 Default Designations**: CEO, Manager, Developer, HR roles, and more
- **6 Leave Types**: Annual, Sick, Casual, LWP, Maternity, Paternity
- **Shift Configuration**: Default 9 AM - 6 PM shift
- **Salary Components**: Basic, HRA, Transport, Medical allowances

### 📧 Automated Notifications
- Birthday reminders
- Probation ending alerts
- Leave balance notifications
- Welcome emails for new employees

### 🎨 Custom Roles
- HR Manager Suite
- HR User Suite
- Employee Self Service

### 📊 Dashboard & Reports
- HR Suite Dashboard
- Real-time HR statistics
- Leave tracking
- Attendance monitoring

## 📦 Installation

### Prerequisites
- Frappe Framework (v14+)
- ERPNext (v14+)
- Python 3.10+

### Method 1: Quick Installation (Recommended)

```bash
# Navigate to your bench directory
cd frappe-bench

# Get the HR Suite app
bench get-app https://github.com/macrobian88/hr_suite

# Install to your site
bench --site your-site-name install-app hr_suite

# Restart bench
bench restart
```

### Method 2: Development Installation

```bash
# Clone the repository
cd frappe-bench/apps
git clone https://github.com/macrobian88/hr_suite

# Install dependencies
cd hr_suite
pip install -e .

# Install to site
bench --site your-site-name install-app hr_suite

# Restart
bench restart
```

### Method 3: One-Click Install Script

Create a file `install_hr_suite.sh`:

```bash
#!/bin/bash

echo "=========================================="
echo "HR Suite - One Click Installer"
echo "=========================================="

read -p "Enter your site name: " SITE_NAME

echo "Installing HR Suite on $SITE_NAME..."

# Install ERPNext if not present
if ! bench --site $SITE_NAME list-apps | grep -q "erpnext"; then
    echo "Installing ERPNext..."
    bench get-app erpnext --branch version-14
    bench --site $SITE_NAME install-app erpnext
fi

# Install HRMS
if ! bench --site $SITE_NAME list-apps | grep -q "hrms"; then
    echo "Installing HRMS..."
    bench get-app hrms --branch version-14
    bench --site $SITE_NAME install-app hrms
fi

# Install HR Suite
bench get-app https://github.com/macrobian88/hr_suite
bench --site $SITE_NAME install-app hr_suite
bench --site $SITE_NAME migrate
bench build --app hr_suite
bench restart

echo "✅ HR Suite installed successfully!"
```

Make it executable and run:
```bash
chmod +x install_hr_suite.sh
./install_hr_suite.sh
```

## 🎯 What Gets Configured Automatically?

Upon installation, HR Suite automatically configures:

### 1. Departments
- Human Resources
- Operations
- Finance
- Sales
- Marketing
- IT
- Administration
- Customer Support

### 2. Designations
- CEO
- Manager
- Senior Developer
- Developer
- HR Manager
- HR Executive
- Sales Manager
- Sales Executive
- Marketing Manager
- Marketing Executive
- Accountant
- Admin

### 3. Leave Types
| Leave Type | Days | Carry Forward | Applicable After |
|------------|------|---------------|------------------|
| Annual Leave | 21 | Yes | 90 days |
| Sick Leave | 12 | No | Immediate |
| Casual Leave | 7 | No | Immediate |
| Leave Without Pay | Unlimited | No | Immediate |
| Maternity Leave | 90 | No | 180 days |
| Paternity Leave | 5 | No | 180 days |

### 4. Shift Types
- **General Shift**: 9:00 AM - 6:00 PM
- Auto-attendance enabled
- Half-day threshold: 4 hours

### 5. Salary Components
**Earnings:**
- Basic Salary (Taxable)
- Housing Allowance (Taxable)
- Transport Allowance (Taxable)
- Medical Allowance (Non-Taxable)

**Deductions:**
- Income Tax
- Professional Tax

### 6. Email Templates
- Welcome Email
- Leave Approval Notification

### 7. HR Settings
- Leave approver mandatory
- Email notifications enabled
- Payroll based on attendance
- Birthday reminders enabled

## 💼 Usage

### For HR Managers

1. **Access HR Suite Dashboard**
   ```
   Desk > HR Suite > Dashboard
   ```

2. **Add New Employees**
   ```
   HR Suite > Employee > New
   ```
   - User account created automatically
   - Welcome email sent automatically
   - Leaves allocated automatically

3. **Manage Leaves**
   - Approve/reject leave applications
   - View leave calendar
   - Check leave balances

4. **Process Payroll**
   - Create salary structures using pre-configured components
   - Generate salary slips
   - Email salary slips to employees

### For Employees

1. **Self-Service Portal**
   - Apply for leaves
   - View leave balance
   - Check attendance
   - Download pay slips

2. **Leave Application**
   ```
   HR Suite > Leave Application > New
   ```
   - Select leave type
   - Choose dates
   - Submit for approval

## 🔧 Configuration

### Customizing Default Settings

After installation, you can customize:

1. **Modify Departments**
   ```
   HR > Department
   ```

2. **Adjust Leave Types**
   ```
   HR > Leave Type
   ```

3. **Update Salary Components**
   ```
   Payroll > Salary Component
   ```

4. **Configure Email Templates**
   ```
   Setup > Email > Email Template
   ```

## 📅 Scheduled Tasks

HR Suite runs the following automated tasks:

### Daily Tasks
- **Birthday Reminders**: Sends birthday wishes to employees
- **Probation Alerts**: Notifies HR managers 7 days before probation ends
- **Leave Balance**: Quarterly reminders to employees about unused leaves

## 🎨 Customization

### Adding Custom Fields

```python
# In your custom app
from frappe import _

def add_custom_fields():
    custom_fields = {
        "Employee": [
            {
                "fieldname": "custom_field",
                "label": _("Custom Field"),
                "fieldtype": "Data",
                "insert_after": "field_name"
            }
        ]
    }
    create_custom_fields(custom_fields)
```

### Extending Functionality

Create a custom app that extends HR Suite:

```python
# hooks.py
app_name = "custom_hr"
required_apps = ["hr_suite", "erpnext"]

# Override HR Suite functions
override_whitelisted_methods = {
    "hr_suite.api.employee.after_employee_insert": "custom_hr.overrides.custom_employee_insert"
}
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: Installation fails with "ERPNext not found"
```bash
# Solution: Install ERPNext first
bench get-app erpnext --branch version-14
bench --site your-site install-app erpnext
```

**Issue**: Email templates not working
```bash
# Solution: Check email settings
bench --site your-site set-config mail_server "smtp.gmail.com"
bench --site your-site set-config mail_port 587
```

**Issue**: Scheduled tasks not running
```bash
# Solution: Enable scheduler
bench --site your-site enable-scheduler
bench restart
```

## 📚 Documentation

For more detailed documentation, visit:
- [Frappe Documentation](https://frappeframework.com/docs)
- [ERPNext HR Documentation](https://docs.erpnext.com/docs/user/manual/en/human-resources)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](license.txt) file for details.

## 🙏 Acknowledgments

- Built on [Frappe Framework](https://frappeframework.com)
- Extends [ERPNext](https://erpnext.com)
- Inspired by the needs of modern HR departments

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/macrobian88/hr_suite/issues)
- **Discussions**: [GitHub Discussions](https://github.com/macrobian88/hr_suite/discussions)
- **Email**: support@yourcompany.com

## 🚀 Roadmap

- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration
- [ ] AI-powered leave predictions
- [ ] Performance management module
- [ ] Training and development tracking

## ⭐ Star Us!

If you find HR Suite helpful, please give us a star on GitHub! It helps others discover the project.

---

<div align="center">
  Made with ❤️ for the HR Community
</div>
