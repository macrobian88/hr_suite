# HR Suite - Frappe Cloud Installation Guide

## 🚨 Important: Frappe Cloud Limitation

**TL;DR:** On Frappe Cloud, you must manually add ERPNext and HRMS to your bench through the UI **before** installing HR Suite. HR Suite will detect if they're missing and guide you.

**Why?** Frappe Cloud's architecture prevents apps from programmatically adding other apps to benches. This is a security and platform design limitation.

**Good News:** On self-hosted installations, HR Suite **automatically installs ERPNext and HRMS** if they're missing! ✨

---

## 🌥️ Frappe Cloud Installation (Required Steps)

### **Step 1: Add Apps to Your Bench**

You need to add all 3 apps to your bench:

#### **1.1 Add ERPNext**
1. Go to **Dashboard → Benches → [Your Bench] → Apps**
2. Click **"Add App"**
3. Repository: `https://github.com/frappe/erpnext`
4. Branch: `version-15`
5. Click **"Add App"**
6. ⏳ Wait 5-10 minutes for build

#### **1.2 Add HRMS**
1. Click **"Add App"**
2. Repository: `https://github.com/frappe/hrms`
3. Branch: `version-15`
4. Click **"Add App"**
5. ⏳ Wait 3-5 minutes for build

#### **1.3 Add HR Suite**
1. Click **"Add App"**
2. Repository: `https://github.com/macrobian88/hr_suite`
3. Branch: `main`
4. Click **"Add App"**
5. ⏳ Wait 2-3 minutes for build

### **Step 2: Install to Your Site (In Order!)**

1. Go to **Dashboard → Sites → [Your Site] → Apps**

2. **Install ERPNext** (First)
   - Find "ERPNext"
   - Click **"Install"**
   - ⏳ Wait 3-5 minutes
   - ✅ Verify success

3. **Install HRMS** (Second)
   - Find "HRMS"
   - Click **"Install"**
   - ⏳ Wait 2-3 minutes
   - ✅ Verify success

4. **Install HR Suite** (Third)
   - Find "HR Suite"
   - Click **"Install"**
   - ⏳ HR Suite will:
     - ✅ Detect ERPNext is installed
     - ✅ Detect HRMS is installed
     - ✅ Automatically configure everything
     - ✅ Create departments, designations, leave types, etc.
   - 🎉 **Done!**

---

## ⚠️ What If I Forget to Install ERPNext/HRMS?

Don't worry! HR Suite is smart:

### **If You Try to Install HR Suite Without Dependencies:**

You'll see a **helpful error message** that shows:
- ✅ Which apps are missing
- ✅ Exact repository URLs to add
- ✅ Step-by-step instructions
- ✅ What to do next

**Example Error:**
```
⚠️ Missing Required Apps

HR Suite requires the following apps:
- ERPNext (https://github.com/frappe/erpnext, version-15)
- HRMS (https://github.com/frappe/hrms, version-15)

Quick Fix:
1. Go to Benches → [Your Bench] → Apps
2. Add the missing apps
3. Go to Sites → [Your Site] → Apps  
4. Install ERPNext and HRMS
5. Then install HR Suite
```

Simply follow the instructions and retry!

---

## 🖥️ Self-Hosted Installation (Fully Automatic!)

### **One Command - Everything Auto-Installs! ✨**

```bash
cd frappe-bench
bench get-app https://github.com/macrobian88/hr_suite
bench --site your-site.local install-app hr_suite
bench restart
```

### **What Happens Automatically:**

```
1. 🔍 HR Suite checks if ERPNext is installed
   ✖ Not found?
   📦 Downloads ERPNext (version-15)
   📦 Installs ERPNext to your site
   ✅ Done!

2. 🔍 HR Suite checks if HRMS is installed
   ✖ Not found?
   📦 Downloads HRMS (version-15)
   📦 Installs HRMS to your site
   ✅ Done!

3. 🚀 HR Suite installs itself
   ⚙️ Configures everything automatically
   🎉 Ready to use!
```

**No manual steps needed!** 🎉

---

## 🆚 Frappe Cloud vs Self-Hosted

| Feature | Frappe Cloud | Self-Hosted |
|---------|--------------|-------------|
| **Auto-Download Apps** | ❌ No (UI only) | ✅ Yes |
| **Auto-Install Apps** | ❌ No (UI only) | ✅ Yes |
| **Dependency Check** | ✅ Yes (with guidance) | ✅ Yes (auto-fix) |
| **Configuration** | ✅ Automatic | ✅ Automatic |
| **Installation Steps** | 3 apps manually | 1 command |

**Why the difference?**
- Frappe Cloud has security restrictions
- Apps can't modify benches programmatically
- This is by design for platform stability

---

## ✅ Verification

After installation, verify everything worked:

### **Check 1: Apps Installed**
```
Desk → Settings → About
Should see:
  ✅ frappe
  ✅ erpnext
  ✅ hrms
  ✅ hr_suite
```

### **Check 2: Default Data Created**
```
HR → Department
  ✅ 8 departments

HR → Designation
  ✅ 12 designations

HR → Leave Type
  ✅ 6 leave types
```

### **Check 3: Dashboard Works**
```
HR Suite → Dashboard
  ✅ Statistics displayed
  ✅ Quick actions visible
```

---

## 🐛 Troubleshooting

### **Issue: "Missing Required Apps" on Frappe Cloud**

**This is expected!** Just follow the instructions in the error message:
1. Add ERPNext to bench
2. Add HRMS to bench
3. Install both to site
4. Then install HR Suite

### **Issue: Build Failed on Frappe Cloud**

**Solution:**
- Check build logs
- Ensure you're using correct branches:
  - ERPNext: `version-15`
  - HRMS: `version-15`
  - HR Suite: `main`

### **Issue: Auto-install Failed on Self-Hosted**

**Solution:** Install manually:
```bash
cd frappe-bench
bench get-app erpnext --branch version-15
bench get-app hrms --branch version-15
bench --site your-site install-app erpnext
bench --site your-site install-app hrms
bench --site your-site install-app hr_suite
bench restart
```

---

## 📊 What Gets Installed

### **Automatically Installed (Self-Hosted Only):**
- ERPNext v15
- HRMS v15

### **Automatically Configured (Both Platforms):**
- 8 Departments
- 12 Designations
- 6 Leave Types
- 1 Shift Type (9 AM - 6 PM)
- 6 Salary Components
- 3 Custom Roles
- Email Templates
- HR Dashboard

---

## 🔗 Quick Reference

### **Repository URLs:**
```
ERPNext:  https://github.com/frappe/erpnext
HRMS:     https://github.com/frappe/hrms
HR Suite: https://github.com/macrobian88/hr_suite
```

### **Branches:**
```
ERPNext:  version-15
HRMS:     version-15
HR Suite: main
```

### **Installation Order (Frappe Cloud):**
```
1. Add all 3 apps to bench
2. Install ERPNext to site
3. Install HRMS to site
4. Install HR Suite to site
```

### **Installation Command (Self-Hosted):**
```bash
bench get-app https://github.com/macrobian88/hr_suite
bench --site your-site install-app hr_suite
```

---

## 🎯 Next Steps

After installation:

1. **Access Dashboard**
   - HR Suite → Dashboard

2. **Configure Company**
   - Setup → Company

3. **Setup Email**
   - Setup → Email Account

4. **Add Employees**
   - HR Suite → Add New Employee

5. **Start Using!**
   - Everything is pre-configured! 🎉

---

## 📞 Support

- **GitHub Issues**: https://github.com/macrobian88/hr_suite/issues
- **Frappe Forum**: https://discuss.frappe.io
- **Documentation**: https://github.com/macrobian88/hr_suite

---

<div align="center">
  <h3>🎉 Happy HR Management!</h3>
  <p><strong>Self-Hosted:</strong> Fully automatic | <strong>Frappe Cloud:</strong> 3 simple steps</p>
</div>