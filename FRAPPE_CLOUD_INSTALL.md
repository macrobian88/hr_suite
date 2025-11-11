# HR Suite - Frappe Cloud Installation Guide

Complete guide for installing HR Suite on Frappe Cloud.

## 🌥️ Prerequisites

- ✅ Active Frappe Cloud account
- ✅ A bench created (or create a new one)
- ✅ Appropriate plan that allows custom apps

## 📋 Installation Steps

### **Step 1: Add Apps to Your Bench**

You need to add apps in this specific order:

#### **1.1 Add ERPNext**

1. Go to **Dashboard → Benches → [Your Bench]**
2. Click **"Apps"** tab
3. Click **"Add App"** button
4. Fill in:
   - **Repository URL**: `https://github.com/frappe/erpnext`
   - **Branch**: `version-15` (recommended) or `version-14`
5. Click **"Add App"**
6. ⏳ Wait for build to complete (5-10 minutes)

#### **1.2 Add HRMS**

1. Click **"Add App"** button again
2. Fill in:
   - **Repository URL**: `https://github.com/frappe/hrms`
   - **Branch**: `version-15` (recommended) or `version-14`
3. Click **"Add App"**
4. ⏳ Wait for build to complete (3-5 minutes)

#### **1.3 Add HR Suite**

1. Click **"Add App"** button again
2. Fill in:
   - **Repository URL**: `https://github.com/macrobian88/hr_suite`
   - **Branch**: `main`
3. Click **"Add App"**
4. ⏳ Wait for build to complete (2-3 minutes)

### **Step 2: Create or Select a Site**

#### **Option A: Create New Site**

1. Go to **Dashboard → Sites**
2. Click **"New Site"**
3. Fill in:
   - **Subdomain**: your-company-name
   - **Select Bench**: Choose the bench with all apps
   - **Select Plan**: Choose appropriate plan
4. Click **"Create Site"**
5. ⏳ Wait for site creation (5-10 minutes)

#### **Option B: Use Existing Site**

1. Go to **Dashboard → Sites**
2. Select your existing site
3. Proceed to Step 3

### **Step 3: Install Apps to Your Site**

Install apps in this specific order:

#### **3.1 Install ERPNext**

1. Go to **Sites → [Your Site] → Apps**
2. Find **ERPNext** in available apps
3. Click **"Install"**
4. ⏳ Wait for installation (3-5 minutes)
5. ✅ Verify installation is complete

#### **3.2 Install HRMS**

1. Find **HRMS** in available apps
2. Click **"Install"**
3. ⏳ Wait for installation (2-3 minutes)
4. ✅ Verify installation is complete

#### **3.3 Install HR Suite**

1. Find **HR Suite** in available apps
2. Click **"Install"**
3. ⏳ Wait for installation (1-2 minutes)
4. ✅ Installation complete!

### **Step 4: Access HR Suite**

1. Go to your site: `https://your-company-name.frappe.cloud`
2. Login with your credentials
3. Click **"Desk"** (top left)
4. Find **"HR Suite"** module
5. Click **"HR Suite Dashboard"**

## ✅ Verification

After installation, verify everything is working:

### **Check 1: Verify Default Data**

```
HR → Department
  ✓ Should show 8 departments
  
HR → Designation
  ✓ Should show 12 designations
  
HR → Leave Type
  ✓ Should show 6 leave types
```

### **Check 2: Test Dashboard**

```
HR Suite → Dashboard
  ✓ Should display statistics
  ✓ Should show quick action buttons
```

### **Check 3: Create Test Employee**

```
HR Suite → Add New Employee
  ✓ Create a test employee
  ✓ Check if user account is created
  ✓ Check if leaves are allocated
```

## 🐛 Troubleshooting

### **Issue: "Required app not found on bench"**

**Error Message:**
```
hr_suite has a dependency on the app erpnext which was not found on your bench.
```

**Solution:**
1. Make sure ERPNext is added to your bench FIRST
2. Then add HRMS
3. Finally add HR Suite
4. The order matters!

### **Issue: "App installation failed"**

**Solution:**
1. Check if ERPNext and HRMS are installed on the site
2. Go to Site → Logs → Error Log
3. Check for specific error messages
4. Contact support with error details

### **Issue: "Cannot add custom app"**

**Reason:** Your Frappe Cloud plan may not support custom apps

**Solution:**
- Free tier: Does not support custom apps
- Upgrade to Standard or higher plan
- Or contact Frappe Cloud sales

### **Issue: "Build taking too long"**

**Solution:**
1. Builds can take 10-15 minutes
2. Check build status in bench
3. If stuck >30 minutes, cancel and retry
4. Check Frappe Cloud status page

### **Issue: "Welcome emails not sending"**

**Solution:**
1. Configure email settings in your site
2. Go to: Setup → Email Account
3. Configure SMTP settings
4. Test email delivery

## 📊 What Gets Installed

When HR Suite is installed, you automatically get:

### **Master Data**
- 8 Departments (HR, Operations, Finance, Sales, Marketing, IT, Administration, Customer Support)
- 12 Designations (CEO, Manager, Developer, HR roles, etc.)
- 6 Leave Types (Annual, Sick, Casual, LWP, Maternity, Paternity)
- 1 Shift Type (General Shift: 9 AM - 6 PM)
- 6 Salary Components (Basic, HRA, Transport, Medical, Income Tax, Professional Tax)

### **Roles**
- HR Manager Suite
- HR User Suite
- Employee Self Service

### **Features**
- Automated employee onboarding
- Welcome email templates
- Leave management
- Dashboard with statistics
- Employee self-service portal
- Scheduled reminders

## 🔗 Useful Links

- **Your Site**: `https://your-company-name.frappe.cloud`
- **HR Dashboard**: `https://your-company-name.frappe.cloud/app/hr-suite-dashboard`
- **Employee Portal**: `https://your-company-name.frappe.cloud/hr-portal`
- **Frappe Cloud Docs**: https://docs.frappecloud.com
- **HR Suite Repository**: https://github.com/macrobian88/hr_suite

## 🎯 Next Steps

After successful installation:

1. **Configure Company Settings**
   - Setup → Company
   - Update company details

2. **Configure Email**
   - Setup → Email Account
   - Add SMTP settings

3. **Set Holiday List**
   - HR → Holiday List
   - Create/update for your region

4. **Add Employees**
   - HR Suite → Add New Employee
   - Start onboarding your team

5. **Setup Payroll**
   - Payroll → Salary Structure
   - Create salary structures

## 💡 Pro Tips

1. **Use Staging First**
   - If available, test on staging site first
   - Then deploy to production

2. **Monitor Builds**
   - Watch build progress in Bench → Builds
   - Check logs if build fails

3. **Backup Before Installing**
   - Frappe Cloud auto-backups
   - Take manual backup for peace of mind

4. **Check Version Compatibility**
   - Use version-15 for latest features
   - Use version-14 for stability

## 📞 Support

Need help?

- **Frappe Cloud Support**: support@frappe.cloud
- **GitHub Issues**: https://github.com/macrobian88/hr_suite/issues
- **Frappe Forum**: https://discuss.frappe.io
- **Documentation**: https://github.com/macrobian88/hr_suite

## 🎉 Success!

Once installed, you'll have a fully functional HR management system with:
- ✅ Automated onboarding
- ✅ Leave management
- ✅ Attendance tracking
- ✅ Payroll processing
- ✅ Employee self-service
- ✅ Real-time dashboard

**Happy HR Management! 🚀**