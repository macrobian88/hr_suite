#!/bin/bash
# complete_setup.sh - Complete HR Suite Setup Script

set -e

echo "=========================================="
echo "  HR Suite - Complete Setup Script"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

# Check if running in frappe-bench
if [ ! -d "apps" ] || [ ! -d "sites" ]; then
    print_error "This script must be run from frappe-bench directory"
    exit 1
fi

# Get site name
if [ -z "$1" ]; then
    read -p "Enter your site name: " SITE_NAME
else
    SITE_NAME=$1
fi

echo ""
echo "Installing HR Suite on: $SITE_NAME"
echo ""

# Check if site exists
if [ ! -d "sites/$SITE_NAME" ]; then
    print_error "Site $SITE_NAME does not exist"
    exit 1
fi

# Step 1: Check ERPNext
echo "[1/8] Checking ERPNext..."
if ! bench --site $SITE_NAME list-apps | grep -q "erpnext"; then
    print_warning "ERPNext not found. Installing ERPNext..."
    bench get-app erpnext --branch version-14
    bench --site $SITE_NAME install-app erpnext
    print_success "ERPNext installed"
else
    print_success "ERPNext already installed"
fi

# Step 2: Check HRMS
echo "[2/8] Checking HRMS..."
if ! bench --site $SITE_NAME list-apps | grep -q "hrms"; then
    print_warning "HRMS not found. Installing HRMS..."
    bench get-app hrms --branch version-14
    bench --site $SITE_NAME install-app hrms
    print_success "HRMS installed"
else
    print_success "HRMS already installed"
fi

# Step 3: Get HR Suite
echo "[3/8] Getting HR Suite app..."
if [ -d "apps/hr_suite" ]; then
    print_warning "HR Suite already exists, pulling latest changes..."
    cd apps/hr_suite
    git pull
    cd ../..
else
    bench get-app https://github.com/macrobian88/hr_suite
fi
print_success "HR Suite app ready"

# Step 4: Install HR Suite
echo "[4/8] Installing HR Suite..."
bench --site $SITE_NAME install-app hr_suite
print_success "HR Suite installed"

# Step 5: Run migrations
echo "[5/8] Running migrations..."
bench --site $SITE_NAME migrate
print_success "Migrations completed"

# Step 6: Build assets
echo "[6/8] Building assets..."
bench build --app hr_suite
print_success "Assets built"

# Step 7: Clear cache
echo "[7/8] Clearing cache..."
bench --site $SITE_NAME clear-cache
bench --site $SITE_NAME clear-website-cache
print_success "Cache cleared"

# Step 8: Restart
echo "[8/8] Restarting services..."
bench restart
print_success "Services restarted"

echo ""
echo "=========================================="
print_success "HR Suite installation completed!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Open your browser: http://$SITE_NAME"
echo "2. Login with your credentials"
echo "3. Navigate to: HR Suite Dashboard"
echo "4. Start managing your HR operations!"
echo ""
echo "Default Roles Created:"
echo "  - HR Manager Suite"
echo "  - HR User Suite"
echo "  - Employee Self Service"
echo ""
echo "Employee Portal: http://$SITE_NAME/hr-portal"
echo ""