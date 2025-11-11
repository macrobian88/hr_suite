# HR Suite - Quick Start Guide

Get up and running with HR Suite in minutes!

## Prerequisites

Before you begin, ensure you have:

- ✅ Frappe Framework v14+ installed
- ✅ A Frappe bench setup
- ✅ A site created (e.g., `mysite.local`)
- ✅ Administrator access to your site

## Installation (5 Minutes)

### Option 1: Automatic Installation (Recommended)

```bash
# Navigate to your bench directory
cd frappe-bench

# Download and run the installer
wget https://raw.githubusercontent.com/macrobian88/hr_suite/main/install_hr_suite.sh
chmod +x install_hr_suite.sh
./install_hr_suite.sh
```

When prompted, enter your site name (e.g., `mysite.local`).

### Option 2: Manual Installation

```bash
# Get the app
bench get-app https://github.com/macrobian88/hr_suite

# Install to your site
bench --site mysite.local install-app hr_suite

# Restart
bench restart
```

## First Steps After Installation

### 1. Login to Your Site

Open your browser and navigate to:
```
http://your-site-name:8000
```

Login with your administrator credentials.

### 2. Access HR Suite Dashboard

1. Click on the **Desk** icon (top left)
2. Find **HR Suite** in the modules list
3. Click on **HR Suite Dashboard**

### 3. Add Your First Employee

```
HR Suite Dashboard > Quick Actions > Add New Employee
```

Or navigate to:
```
HR > Employee > New
```

Fill in the required fields:
- First Name
- Last Name (optional)
- Company Email
- Date of Joining
- Department
- Designation

**What happens automatically:**
- ✅ User account created
- ✅ Welcome email sent
- ✅ Leaves allocated
- ✅ Employee Self Service role assigned

### 4. Configure Your Company Settings (Optional)

Navigate to:
```
Setup > Company
```

Update:
- Company name
- Address
- Contact details
- Holiday list

## Key Features You Can Use Immediately

### For HR Managers

#### View Dashboard Statistics
```
HR Suite > Dashboard
```
See:
- Total employees
- Employees on leave today
- Pending leave applications
- New joinings this month

#### Approve Leave Applications
```
HR > Leave Application > Open
```

#### Mark Attendance
```
HR > Attendance > New
```

#### Process Payroll
```
Payroll > Salary Slip > New
```

### For Employees

#### Access Self-Service Portal
```
http://your-site-name:8000/hr-portal
```

#### Apply for Leave
```
HR > Leave Application > New
```

#### Check Leave Balance
```
HR > Leave Ledger Entry
```

#### View Salary Slips
```
Payroll > Salary Slip
```

## What's Already Configured?

### 🏢 Departments (8)
- Human Resources
- Operations
- Finance
- Sales
- Marketing
- IT
- Administration
- Customer Support

### 💼 Designations (12)
- CEO, Manager, Developer, HR roles, and more

### 🌴 Leave Types (6)
| Leave Type | Days | Carry Forward |
|------------|------|---------------|
| Annual Leave | 21 | Yes |
| Sick Leave | 12 | No |
| Casual Leave | 7 | No |
| Leave Without Pay | Unlimited | No |
| Maternity Leave | 90 | No |
| Paternity Leave | 5 | No |

### ⏰ Shift Type
- **General Shift**: 9:00 AM - 6:00 PM

### 💰 Salary Components
- Basic Salary
- Housing Allowance
- Transport Allowance
- Medical Allowance
- Income Tax
- Professional Tax

## Common Tasks

### How to Add Multiple Employees at Once?

```
HR > Employee > Menu > Import
```

Download the template, fill it in, and upload.

### How to Create a Salary Structure?

```
Payroll > Salary Structure > New
```

1. Enter structure name
2. Select company
3. Add salary components
4. Set amounts or formulas
5. Save and submit

### How to Assign Salary Structure to Employees?

```
Payroll > Salary Structure Assignment > New
```

1. Select employee
2. Select salary structure
3. Set from date
4. Save and submit

### How to Process Monthly Salary?

```
Payroll > Payroll Entry > New
```

1. Select company and month
2. Get employees
3. Create salary slips
4. Submit salary slips
5. Make payment entry

## Customization

### Add Custom Department

```
HR > Department > New
```

### Modify Leave Type Settings

```
HR > Leave Type > [Select Leave Type] > Edit
```

### Change Shift Timings

```
HR > Shift Type > General Shift > Edit
```

## Troubleshooting

### Issue: Installation fails

**Solution:**
```bash
# Check if ERPNext is installed
bench --site mysite.local list-apps

# If not, install ERPNext first
bench get-app erpnext --branch version-14
bench --site mysite.local install-app erpnext
```

### Issue: Employee not receiving welcome email

**Solution:**
```bash
# Check email settings
bench --site mysite.local set-config mail_server "smtp.gmail.com"
bench --site mysite.local set-config mail_port 587
bench --site mysite.local set-config mail_login "your-email@gmail.com"
bench --site mysite.local set-config mail_password "your-password"
```

### Issue: Dashboard not showing data

**Solution:**
```bash
# Clear cache
bench --site mysite.local clear-cache
bench restart
```

### Issue: Scheduled tasks not running

**Solution:**
```bash
# Enable scheduler
bench --site mysite.local enable-scheduler
bench restart
```

## Next Steps

1. 📚 Read the [Full Documentation](README.md)
2. 👥 Join our [Community](https://github.com/macrobian88/hr_suite/discussions)
3. 🐛 Report [Issues](https://github.com/macrobian88/hr_suite/issues)
4. ⭐ Star the [Repository](https://github.com/macrobian88/hr_suite)

## Need Help?

- 💬 [GitHub Discussions](https://github.com/macrobian88/hr_suite/discussions)
- 🐛 [Report Bug](https://github.com/macrobian88/hr_suite/issues/new?labels=bug)
- 💡 [Request Feature](https://github.com/macrobian88/hr_suite/issues/new?labels=enhancement)

## Support the Project

If you find HR Suite helpful:
- ⭐ Star the repository
- 👤 Follow for updates
- 👫 Share with others
- 📝 Write about your experience

---

**Happy HR Management! 🚀**