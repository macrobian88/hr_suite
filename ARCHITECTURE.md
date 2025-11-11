# HR Suite - Architecture Documentation

## Overview

HR Suite is built as a Frappe application that extends ERPNext's HR module with automated configuration and enhanced features.

## Technology Stack

- **Framework**: Frappe Framework v14+
- **Backend**: Python 3.10+
- **Frontend**: JavaScript, HTML, CSS
- **Database**: MariaDB/PostgreSQL
- **Base Apps**: ERPNext, HRMS

## Directory Structure

```
hr_suite/
├── hr_suite/                    # Main application directory
│   ├── __init__.py             # Package initialization
│   ├── hooks.py                # Frappe hooks configuration
│   ├── install.py              # Installation and setup logic
│   ├── tasks.py                # Scheduled background tasks
│   ├── setup_wizard.py         # Setup wizard configuration
│   ├── modules.txt             # Module definitions
│   ├── patches.txt             # Database patches
│   │
│   ├── api/                    # API endpoints
│   │   ├── __init__.py
│   │   └── employee.py         # Employee-related APIs
│   │
│   ├── config/                 # Configuration files
│   │   ├── __init__.py
│   │   ├── desktop.py          # Desktop/workspace config
│   │   └── docs.py             # Documentation config
│   │
│   ├── fixtures/               # Data fixtures
│   │   └── role.json           # Default roles
│   │
│   ├── patches/                # Database migration patches
│   │   ├── __init__.py
│   │   └── v1_0/
│   │       ├── __init__.py
│   │       └── setup_hr_suite.py
│   │
│   ├── public/                 # Static assets
│   │   ├── css/
│   │   │   └── hr_suite.css
│   │   └── js/
│   │       └── hr_suite.js
│   │
│   ├── templates/              # Jinja templates
│   │   └── __init__.py
│   │
│   ├── www/                    # Web pages
│   │   ├── __init__.py
│   │   └── hr-portal/
│   │       ├── __init__.py
│   │       └── index.html
│   │
│   └── hr_suite_dashboard/     # Dashboard module
│       ├── __init__.py
│       └── page/
│           ├── __init__.py
│           └── hr_suite_dashboard/
│               ├── __init__.py
│               ├── hr_suite_dashboard.json
│               ├── hr_suite_dashboard.js
│               └── hr_suite_dashboard.py
│
├── install_hr_suite.sh         # Quick installation script
├── complete_setup.sh           # Complete setup script
├── setup.py                    # Python package setup
├── requirements.txt            # Python dependencies
├── license.txt                 # MIT License
├── README.md                   # Main documentation
├── QUICKSTART.md               # Quick start guide
├── CONTRIBUTING.md             # Contribution guidelines
├── CHANGELOG.md                # Version history
└── .gitignore                  # Git ignore rules
```

## Core Components

### 1. Installation Module (`install.py`)

**Purpose**: Automates the complete setup process

**Key Functions**:
- `after_install()` - Main installation orchestrator
- `create_hr_roles()` - Creates custom roles
- `setup_hr_settings()` - Configures HR settings
- `create_default_departments()` - Sets up departments
- `create_default_designations()` - Creates designations
- `setup_leave_types()` - Configures leave types
- `setup_attendance_settings()` - Sets up attendance
- `setup_payroll_settings()` - Configures payroll
- `setup_email_templates()` - Creates email templates

**Flow**:
```
Installation Triggered
        ↓
Check Dependencies
        ↓
Create Roles
        ↓
Setup HR Settings
        ↓
Create Master Data (Departments, Designations)
        ↓
Configure Leave System
        ↓
Setup Attendance & Payroll
        ↓
Create Email Templates
        ↓
Build Dashboard
        ↓
Complete
```

### 2. Employee API (`api/employee.py`)

**Purpose**: Handles employee lifecycle events

**Key Functions**:
- `after_employee_insert()` - Triggered when new employee is created
- `send_welcome_email()` - Sends automated welcome email
- `create_user_account()` - Creates Frappe user account
- `allocate_leaves()` - Auto-allocates leave balances

**Event Flow**:
```
New Employee Created
        ↓
after_employee_insert() Triggered
        ↓
Send Welcome Email
        ↓
Create User Account
        ↓
Assign Roles
        ↓
Allocate Leaves
```

### 3. Scheduled Tasks (`tasks.py`)

**Purpose**: Background automation

**Tasks**:
- `daily_hr_reminders()` - Daily task runner
- `send_birthday_reminders()` - Birthday notifications
- `send_probation_reminders()` - Probation ending alerts
- `send_leave_balance_reminders()` - Leave balance updates

**Schedule**:
```
Daily at 9:00 AM
    ↓
Check Birthdays
    ↓
Check Probation End Dates
    ↓
Send Notifications
```

### 4. Dashboard (`hr_suite_dashboard/`)

**Purpose**: Real-time HR metrics visualization

**Components**:
- `hr_suite_dashboard.py` - Backend API
- `hr_suite_dashboard.js` - Frontend rendering
- `hr_suite_dashboard.json` - Page configuration

**API Endpoints**:
- `get_hr_stats()` - Returns dashboard statistics

**Metrics**:
- Total active employees
- Employees on leave today
- Pending leave applications
- New joinings this month
- Upcoming birthdays
- Probation ending soon

## Data Flow

### Employee Onboarding Flow

```
HR Manager Creates Employee
        ↓
Employee Document Saved
        ↓
after_employee_insert() Hook Triggered
        ↓
├── Create User Account
│       ↓
│   Set Email & Name
│       ↓
│   Assign "Employee Self Service" Role
│
├── Send Welcome Email
│       ↓
│   Load Email Template
│       ↓
│   Populate Variables
│       ↓
│   Send via SMTP
│
└── Allocate Leaves
        ↓
    For Each Leave Type
        ↓
    Create Leave Allocation
        ↓
    Submit Document
```

### Leave Application Flow

```
Employee Applies for Leave
        ↓
Leave Application Created
        ↓
Validation
    ↓
├── Check Leave Balance
├── Check Approver
├── Check Overlapping Leaves
└── Check Block Dates
        ↓
Submit for Approval
        ↓
Notification to Approver
        ↓
Approver Reviews
        ↓
├── Approve → Update Leave Ledger
└── Reject → Notify Employee
```

## Hooks System

### Document Hooks (`hooks.py`)

```python
doc_events = {
    "Employee": {
        "after_insert": "hr_suite.api.employee.after_employee_insert"
    }
}
```

### Scheduled Hooks

```python
scheduler_events = {
    "daily": [
        "hr_suite.tasks.daily_hr_reminders"
    ]
}
```

## Security

### Role-Based Access Control

**Roles**:
1. **HR Manager Suite**
   - Full access to all HR functions
   - Can approve/reject leave applications
   - Can view all employee data
   - Can process payroll

2. **HR User Suite**
   - Can create/edit employees
   - Can view reports
   - Limited payroll access

3. **Employee Self Service**
   - Can view own data
   - Can apply for leave
   - Can view own pay slips
   - Can mark attendance

### Permission Structure

```
Employee Doctype
├── HR Manager Suite: All permissions
├── HR User Suite: Read, Write, Create
└── Employee Self Service: Read (own documents only)

Leave Application
├── HR Manager Suite: All permissions
├── HR User Suite: Read, Create
└── Employee Self Service: Read (own), Create
```

## Database Schema

### Custom Fields

HR Suite doesn't add custom fields by default but can be extended:

```python
custom_fields = {
    "Employee": [
        {
            "fieldname": "custom_field_name",
            "label": "Field Label",
            "fieldtype": "Data",
            "insert_after": "existing_field"
        }
    ]
}
```

## API Integration

### REST API Endpoints

All Frappe REST API endpoints are available:

```
GET /api/resource/Employee
GET /api/resource/Employee/{employee_id}
POST /api/resource/Employee
PUT /api/resource/Employee/{employee_id}
DELETE /api/resource/Employee/{employee_id}
```

### Custom API Methods

```python
@frappe.whitelist()
def get_hr_stats():
    # Custom implementation
    return stats
```

Access via:
```
POST /api/method/hr_suite.hr_suite_dashboard.page.hr_suite_dashboard.hr_suite_dashboard.get_hr_stats
```

## Performance Considerations

### Caching

- Dashboard statistics cached for 5 minutes
- Employee lists cached at document level
- Leave balance calculated on-demand

### Optimization

- Use of database indexes on frequently queried fields
- Batch processing for bulk operations
- Async email sending
- Lazy loading of dashboard widgets

## Testing

### Unit Tests

```bash
bench --site test.local run-tests --app hr_suite
```

### Test Structure

```
hr_suite/tests/
├── __init__.py
├── test_employee.py
├── test_leave_allocation.py
└── test_dashboard.py
```

## Deployment

### Production Checklist

- [ ] Install ERPNext and HRMS
- [ ] Configure email settings
- [ ] Enable scheduler
- [ ] Set up backup schedule
- [ ] Configure SSL
- [ ] Set up monitoring

### Scaling

- Use Redis for caching
- Enable database read replicas
- Use background workers for heavy tasks
- Implement CDN for static assets

## Troubleshooting

### Common Issues

1. **Scheduler not running**
   ```bash
   bench --site mysite.local enable-scheduler
   ```

2. **Emails not sending**
   - Check email configuration
   - Verify SMTP settings
   - Check email queue

3. **Dashboard not loading**
   - Clear cache
   - Check browser console
   - Verify API endpoint

## Future Architecture Plans

- Microservices architecture for scalability
- GraphQL API support
- Real-time notifications via WebSockets
- Machine learning for predictive analytics
- Mobile app integration

---

**Last Updated**: November 2024  
**Version**: 1.0.0