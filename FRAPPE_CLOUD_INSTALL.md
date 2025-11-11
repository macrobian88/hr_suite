# HR Suite - Frappe Cloud Installation Guide

## 🎯 Smart Installation

HR Suite now **automatically detects and guides you** through dependency installation!

### What Happens:

- **On Frappe Cloud**: HR Suite will check if ERPNext and HRMS are installed and show you exactly what to do if they're missing
- **On Self-Hosted**: HR Suite will **automatically install** ERPNext and HRMS if they're not already installed

---

## 🌥️ Frappe Cloud Installation

### **Method 1: Quick Install (Recommended)**

Just add HR Suite to your bench and install it! It will tell you if anything is missing.

#### **Step 1: Add HR Suite to Bench**

1. Go to **Dashboard → Benches → [Your Bench]**
2. Click **"Apps"** tab
3. Click **"Add App"** button
4. Fill in:
   - **Repository URL**: `https://github.com/macrobian88/hr_suite`
   - **Branch**: `main`
5. Click **"Add App"**
6. ⏳ Wait for build (2-3 minutes)

#### **Step 2: Install to Site**

1. Go to **Dashboard → Sites → [Your Site] → Apps**
2. Find **"HR Suite"** in available apps
3. Click **"Install"**

**What will happen:**
- ✅ If ERPNext & HRMS are installed: Installation proceeds smoothly
- ⚠️ If missing: You'll see a helpful message telling you exactly what to install

#### **Step 3: If Dependencies Are Missing**

If you see a message about missing apps, follow these steps:

**a) Add Missing Apps to Bench:**

```
1. Go to: Dashboard → Benches → [Your Bench] → Apps

2. Add ERPNext (if missing):
   Repository: https://github.com/frappe/erpnext
   Branch: version-15
   
3. Add HRMS (if missing):
   Repository: https://github.com/frappe/hrms
   Branch: version-15
```

**b) Install to Your Site:**

```
1. Go to: Dashboard → Sites → [Your Site] → Apps

2. Install ERPNext (if not installed)
   Wait for completion ⏳
   
3. Install HRMS (if not installed)
   Wait for completion ⏳
   
4. Install HR Suite
   Done! ✅
```

---

### **Method 2: Install Everything from Scratch**

If you're starting fresh or want to ensure everything is in order:

#### **1. Add All Apps to Bench**

Go to **Dashboard → Benches → [Your Bench] → Apps**

Add in this order:

```
1. ERPNext
   Repository: https://github.com/frappe/erpnext
   Branch: version-15
   [Add App] → Wait ⏳

2. HRMS
   Repository: https://github.com/frappe/hrms
   Branch: version-15
   [Add App] → Wait ⏳

3. HR Suite
   Repository: https://github.com/macrobian88/hr_suite
   Branch: main
   [Add App] → Wait ⏳
```

#### **2. Create or Select Site**

- **New Site**: Dashboard → Sites → New Site
- **Existing Site**: Dashboard → Sites → [Your Site]

#### **3. Install Apps to Site**

Go to **Sites → [Your Site] → Apps**

Install in this order:

```
1. ERPNext → Click "Install" → Wait ⏳
2. HRMS → Click "Install" → Wait ⏳
3. HR Suite → Click "Install" → Wait ⏳
```

**Done! ✅**

---

## 🖥️ Self-Hosted Installation

### **Super Easy - Fully Automatic!**

On self-hosted, HR Suite will **automatically install ERPNext and HRMS** if they're missing.

#### **One Command Installation:**

```bash
# Navigate to bench
cd frappe-bench

# Get and install HR Suite
bench get-app https://github.com/macrobian88/hr_suite
bench --site your-site.local install-app hr_suite

# That's it! ERPNext and HRMS will be installed automatically if needed
bench restart
```

#### **What Happens Automatically:**

1. ✅ Checks if ERPNext is installed
2. ✅ If not, downloads and installs ERPNext (version-15)
3. ✅ Checks if HRMS is installed
4. ✅ If not, downloads and installs HRMS (version-15)
5. ✅ Installs HR Suite
6. ✅ Configures everything

**No manual steps needed!** 🎉

---

## ✅ Verification

After installation, verify everything is working:

### **Check 1: Verify Apps Installed**

```
Go to: Desk → Settings → About
Check installed apps:
  ✓ frappe
  ✓ erpnext
  ✓ hrms
  ✓ hr_suite
```

### **Check 2: Verify Default Data**

```
HR → Department
  ✓ Should show 8 departments
  
HR → Designation
  ✓ Should show 12 designations
  
HR → Leave Type
  ✓ Should show 6 leave types
```

### **Check 3: Access Dashboard**

```
HR Suite → Dashboard
  ✓ Should display statistics
  ✓ Should show quick action buttons
```

---

## 🆚 Frappe Cloud vs Self-Hosted

| Feature | Frappe Cloud | Self-Hosted |
|---------|--------------|-------------|
| **Dependency Check** | ✅ Shows helpful message | ✅ Auto-installs |
| **ERPNext Installation** | Manual (via UI) | Automatic |
| **HRMS Installation** | Manual (via UI) | Automatic |
| **HR Suite Installation** | Manual (via UI) | Manual (command) |
| **Configuration** | ✅ Automatic | ✅ Automatic |
| **Updates** | ✅ Automatic | Manual (bench update) |

---

## 🐛 Troubleshooting

### **Issue: "Missing Required Apps" Error on Frappe Cloud**

**Error Message:**
```
Missing Required Apps
HR Suite requires the following apps to be installed:
- ERPNext
- HRMS
```

**Solution:**
1. Don't panic! This is intentional
2. Follow the instructions in the error message
3. Add missing apps to your bench
4. Install them to your site
5. Then install HR Suite

### **Issue: "Cannot add custom app" on Frappe Cloud**

**Reason:** Your plan doesn't support custom apps

**Solution:**
- Free tier: Does not support custom apps
- Upgrade to Standard or Business plan
- Or contact Frappe Cloud sales

### **Issue: Auto-installation fails on Self-Hosted**

**Solution:**
```bash
# Install manually
cd frappe-bench
bench get-app erpnext --branch version-15
bench get-app hrms --branch version-15
bench --site your-site install-app erpnext
bench --site your-site install-app hrms
bench --site your-site install-app hr_suite
bench restart
```

### **Issue: Build taking too long**

**Solution:**
- Frappe Cloud builds can take 10-15 minutes
- Check build status in Bench → Builds
- If stuck >30 minutes, cancel and retry

---

## 📊 What Gets Installed

When HR Suite is installed, you automatically get:

### **Dependencies (Auto-handled)**
- ERPNext v15 (if not installed)
- HRMS v15 (if not installed)

### **Master Data**
- 8 Departments
- 12 Designations
- 6 Leave Types
- 1 Shift Type
- 6 Salary Components

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

---

## 🔗 Useful Links

- **Your Site**: `https://your-company.frappe.cloud`
- **HR Dashboard**: `https://your-company.frappe.cloud/app/hr-suite-dashboard`
- **Employee Portal**: `https://your-company.frappe.cloud/hr-portal`
- **Repository**: https://github.com/macrobian88/hr_suite
- **Issues**: https://github.com/macrobian88/hr_suite/issues

---

## 🎯 Next Steps

After successful installation:

1. **Configure Company**
   - Setup → Company → Update details

2. **Configure Email**
   - Setup → Email Account → Add SMTP

3. **Set Holiday List**
   - HR → Holiday List → Create/update

4. **Add Employees**
   - HR Suite → Add New Employee

5. **Setup Payroll**
   - Payroll → Salary Structure → Create

---

## 💡 Pro Tips

### **For Frappe Cloud:**
- ✅ Add all apps to bench before creating sites
- ✅ Use staging site to test first
- ✅ Monitor build logs for any errors
- ✅ Take backup before installing

### **For Self-Hosted:**
- ✅ Just run `bench install-app hr_suite` - it does everything!
- ✅ Ensure internet connection for downloading apps
- ✅ Run `bench update` regularly
- ✅ Check logs if auto-install fails

---

## 📞 Support

Need help?

- **Frappe Cloud Support**: support@frappe.cloud
- **GitHub Issues**: https://github.com/macrobian88/hr_suite/issues
- **Frappe Forum**: https://discuss.frappe.io
- **Documentation**: https://github.com/macrobian88/hr_suite

---

## 🎉 Success!

Once installed, you'll have:
- ✅ Complete HR management system
- ✅ Automated employee onboarding
- ✅ Leave management
- ✅ Attendance tracking
- ✅ Payroll processing
- ✅ Employee self-service
- ✅ Real-time dashboard

**No manual configuration needed!** 🚀

---

<div align="center">
  <strong>Happy HR Management! 🎉</strong>
</div>