# HR Suite - Complete HR Management Solution

<div align="center">
  <img src="https://img.shields.io/badge/Frappe-Framework-blue" alt="Frappe">
  <img src="https://img.shields.io/badge/ERPNext-Compatible-green" alt="ERPNext">
  <img src="https://img.shields.io/badge/Frappe_Cloud-Ready-orange" alt="Frappe Cloud">
  <img src="https://img.shields.io/badge/Auto_Install-Yes-brightgreen" alt="Auto Install">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="License">
  <img src="https://img.shields.io/badge/Version-1.0.0-red" alt="Version">
</div>

## 🎯 Overview

**HR Suite** is a comprehensive HR management solution with **intelligent dependency management**. It automatically detects and installs ERPNext and HRMS if they're not already present, making it truly one-click!

### ⚡ Smart Features

- 🧠 **Intelligent Dependency Detection**: Automatically checks if ERPNext and HRMS are installed
- 🔄 **Auto-Installation** (Self-Hosted): Automatically installs missing dependencies
- 💬 **Helpful Guidance** (Frappe Cloud): Shows exactly what to do if dependencies are missing
- ⚙️ **Zero Configuration**: Everything is pre-configured out of the box
- 🚀 **One-Click Setup**: Install and start using immediately

---

## 🌥️ Installation - Choose Your Platform

### 🎯 Frappe Cloud (Recommended for Beginners)

**Just add HR Suite - it will guide you through the rest!**

```
1. Go to: Benches → [Your Bench] → Apps → Add App
2. Repository: https://github.com/macrobian88/hr_suite
3. Branch: main
4. Install to your site
5. Follow any prompts if dependencies are missing
```

**[📘 Complete Frappe Cloud Guide →](FRAPPE_CLOUD_INSTALL.md)**

### 💻 Self-Hosted (Fully Automatic)

**One command - ERPNext & HRMS install automatically if needed!**

```bash
cd frappe-bench
bench get-app https://github.com/macrobian88/hr_suite
bench --site your-site.local install-app hr_suite
bench restart
```

**That's it!** HR Suite will:
- ✅ Check if ERPNext is installed (auto-install if missing)
- ✅ Check if HRMS is installed (auto-install if missing)
- ✅ Install HR Suite
- ✅ Configure everything automatically

---

## ✨ What Makes HR Suite Special

### 🧠 Smart Dependency Management

| Platform | Behavior |
|----------|----------|
| **Frappe Cloud** | Shows helpful error with exact steps if ERPNext/HRMS missing |
| **Self-Hosted** | **Automatically installs** ERPNext and HRMS if missing |

### 🎁 Pre-Configured Features

Upon installation, HR Suite automatically creates:

- ✅ **8 Departments**: HR, Operations, Finance, Sales, Marketing, IT, Administration, Customer Support
- ✅ **12 Designations**: CEO, Manager, Developer, HR roles, and more
- ✅ **6 Leave Types**: Annual (21 days), Sick (12 days), Casual (7 days), LWP, Maternity (90 days), Paternity (5 days)
- ✅ **1 Shift Type**: General Shift (9 AM - 6 PM)
- ✅ **6 Salary Components**: Basic, HRA, Transport, Medical, Income Tax, Professional Tax
- ✅ **3 Custom Roles**: HR Manager Suite, HR User Suite, Employee Self Service
- ✅ **Email Templates**: Welcome emails, Leave approval notifications
- ✅ **HR Dashboard**: Real-time statistics and quick actions

### 🤖 Automated Workflows

- **Employee Onboarding**: Auto-create user accounts, send welcome emails, allocate leaves
- **Leave Management**: Automated approval workflows and notifications
- **Reminders**: Birthday wishes, probation alerts, leave balance updates
- **Self-Service**: Employee portal for leaves, attendance, payslips

---

## 📦 Detailed Installation

### Option 1: Frappe Cloud

#### Step 1: Add HR Suite to Bench
```
Dashboard → Benches → [Your Bench] → Apps → Add App
Repository: https://github.com/macrobian88/hr_suite
Branch: main
```

#### Step 2: Install to Site
```
Dashboard → Sites → [Your Site] → Apps → Install HR Suite
```

**If you see "Missing Required Apps" error:**
- Don't worry! This is intentional
- The error message tells you exactly what to do
- Add ERPNext and HRMS to your bench
- Install them to your site
- Then install HR Suite

**[📘 Full Frappe Cloud Guide with Screenshots →](FRAPPE_CLOUD_INSTALL.md)**

---

### Option 2: Self-Hosted (Quick Install)

```bash
# Single command installation
cd frappe-bench
bench get-app https://github.com/macrobian88/hr_suite
bench --site your-site.local install-app hr_suite
bench restart
```

**What happens automatically:**
1. Checks for ERPNext → Installs if missing
2. Checks for HRMS → Installs if missing
3. Installs HR Suite
4. Configures all settings
5. Creates master data

---

### Option 3: Manual Installation (Advanced)

If you prefer full control:

```bash
# Install dependencies first
bench get-app erpnext --branch version-15
bench get-app hrms --branch version-15
bench --site your-site.local install-app erpnext
bench --site your-site.local install-app hrms

# Install HR Suite
bench get-app https://github.com/macrobian88/hr_suite
bench --site your-site.local install-app hr_suite
bench restart
```

---

## 🎯 What Gets Configured Automatically?

### 1. Master Data

**Departments (8)**
- Human Resources, Operations, Finance, Sales
- Marketing, IT, Administration, Customer Support

**Designations (12)**
- CEO, Manager, Senior Developer, Developer
- HR Manager, HR Executive, Sales Manager, Sales Executive
- Marketing Manager, Marketing Executive, Accountant, Admin

### 2. Leave Management

| Leave Type | Days | Carry Forward | Applicable After |
|------------|------|---------------|------------------|
| Annual Leave | 21 | ✅ Yes | 90 days |
| Sick Leave | 12 | ❌ No | Immediate |
| Casual Leave | 7 | ❌ No | Immediate |
| Leave Without Pay | ∞ | ❌ No | Immediate |
| Maternity Leave | 90 | ❌ No | 180 days |
| Paternity Leave | 5 | ❌ No | 180 days |

### 3. Attendance & Payroll

**Shift Type**: General Shift (9:00 AM - 6:00 PM)
- Auto-attendance enabled
- Half-day threshold: 4 hours
- Working days: Monday to Friday

**Salary Components**:
- **Earnings**: Basic Salary, HRA, Transport Allowance, Medical Allowance
- **Deductions**: Income Tax, Professional Tax

### 4. Roles & Permissions

- **HR Manager Suite**: Full access to all HR functions
- **HR User Suite**: Limited HR operations
- **Employee Self Service**: Personal data access only

---

## 💼 How to Use

### For HR Managers

**1. Access Dashboard**
```
Desk → HR Suite → Dashboard
```
View real-time statistics:
- Total active employees
- Employees on leave today
- Pending leave applications
- New joinings this month

**2. Add New Employee**
```
HR Suite → Quick Actions → Add New Employee
```
What happens automatically:
- ✅ User account created
- ✅ Welcome email sent
- ✅ Leaves allocated
- ✅ Self-service role assigned

**3. Manage Leaves**
- Approve/reject applications
- View leave calendar
- Check team leave balances

**4. Process Payroll**
- Create salary structures
- Generate salary slips
- Email slips to employees

### For Employees

**1. Self-Service Portal**
```
https://your-site.local/hr-portal
```

**2. Apply for Leave**
```
HR → Leave Application → New
```

**3. View Salary Slips**
```
Payroll → Salary Slip
```

**4. Check Leave Balance**
```
HR → Leave Ledger Entry
```

---

## 📅 Automated Tasks

HR Suite runs background tasks automatically:

### Daily (9:00 AM)
- 🎂 **Birthday Reminders**: Sends wishes to employees
- ⏰ **Probation Alerts**: Notifies HR 7 days before probation ends
- 📊 **Leave Balance**: Quarterly reminders about unused leaves

### Real-time
- 📧 **Welcome Emails**: Sent immediately when employee is created
- 📩 **Leave Notifications**: Instant notifications on approval/rejection

---

## 🐛 Troubleshooting

### Frappe Cloud

**Q: I see "Missing Required Apps" error**  
**A:** This is intentional! Follow the instructions in the error message:
1. Add ERPNext to your bench
2. Add HRMS to your bench
3. Install both to your site
4. Then install HR Suite

[See detailed troubleshooting →](FRAPPE_CLOUD_INSTALL.md#-troubleshooting)

### Self-Hosted

**Q: Auto-installation failed**  
**A:** Install manually:
```bash
bench get-app erpnext --branch version-15
bench get-app hrms --branch version-15
bench --site your-site install-app erpnext
bench --site your-site install-app hrms
bench --site your-site install-app hr_suite
```

**Q: Email templates not working**  
**A:** Configure email settings:
```bash
bench --site your-site set-config mail_server "smtp.gmail.com"
bench --site your-site set-config mail_port 587
bench --site your-site set-config mail_login "your@email.com"
bench --site your-site set-config mail_password "your-password"
```

**Q: Scheduled tasks not running**  
**A:** Enable scheduler:
```bash
bench --site your-site enable-scheduler
bench restart
```

---

## 📚 Documentation

- **[Quick Start Guide](QUICKSTART.md)** - Get started in 5 minutes
- **[Frappe Cloud Installation](FRAPPE_CLOUD_INSTALL.md)** - Cloud-specific guide
- **[Architecture Documentation](ARCHITECTURE.md)** - Technical details
- **[Contributing Guidelines](CONTRIBUTING.md)** - How to contribute
- **[Changelog](CHANGELOG.md)** - Version history

---

## 🚀 Roadmap

- [ ] Multi-language support
- [ ] Advanced analytics dashboard with charts
- [ ] Mobile app integration
- [ ] AI-powered leave predictions
- [ ] Performance management module
- [ ] Training and development tracking
- [ ] Recruitment and onboarding module
- [ ] Employee surveys and feedback

---

## 🤝 Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](license.txt) file for details.

---

## 🙏 Acknowledgments

- Built on [Frappe Framework](https://frappeframework.com)
- Extends [ERPNext](https://erpnext.com) and [HRMS](https://github.com/frappe/hrms)
- Optimized for [Frappe Cloud](https://frappecloud.com)
- Inspired by the needs of modern HR departments

---

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/macrobian88/hr_suite/issues)
- **Discussions**: [GitHub Discussions](https://github.com/macrobian88/hr_suite/discussions)
- **Forum**: [Frappe Forum](https://discuss.frappe.io)
- **Frappe Cloud**: [Installation Guide](FRAPPE_CLOUD_INSTALL.md)

---

## ⭐ Star Us!

If you find HR Suite helpful, please give us a star on GitHub! It helps others discover the project.

[![GitHub stars](https://img.shields.io/github/stars/macrobian88/hr_suite?style=social)](https://github.com/macrobian88/hr_suite/stargazers)

---

<div align="center">
  <h3>Made with ❤️ for the HR Community</h3>
  <p>Smart • Automated • Easy to Use</p>
</div>
