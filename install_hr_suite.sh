#!/bin/bash

echo "=========================================="
echo "HR Suite - One Click Installer"
echo "=========================================="
echo ""

# Get site name
read -p "Enter your site name (e.g., mysite.local): " SITE_NAME

if [ -z "$SITE_NAME" ]; then
    echo "Error: Site name cannot be empty"
    exit 1
fi

echo ""
echo "Installing HR Suite on $SITE_NAME..."
echo ""

# Check if site exists
if ! bench --site $SITE_NAME list-apps &> /dev/null; then
    echo "Error: Site $SITE_NAME not found"
    exit 1
fi

# Install ERPNext if not installed
if ! bench --site $SITE_NAME list-apps | grep -q "erpnext"; then
    echo "ERPNext not found. Installing ERPNext..."
    bench get-app erpnext --branch version-14
    bench --site $SITE_NAME install-app erpnext
    echo "✅ ERPNext installed"
else
    echo "✅ ERPNext already installed"
fi

# Install HRMS if not installed
if ! bench --site $SITE_NAME list-apps | grep -q "hrms"; then
    echo "HRMS not found. Installing HRMS..."
    bench get-app hrms --branch version-14
    bench --site $SITE_NAME install-app hrms
    echo "✅ HRMS installed"
else
    echo "✅ HRMS already installed"
fi

# Get HR Suite
echo "Getting HR Suite..."
bench get-app https://github.com/macrobian88/hr_suite

# Install HR Suite
echo "Installing HR Suite..."
bench --site $SITE_NAME install-app hr_suite

# Migrate
echo "Running migrations..."
bench --site $SITE_NAME migrate

# Build assets
echo "Building assets..."
bench build --app hr_suite

# Clear cache
echo "Clearing cache..."
bench --site $SITE_NAME clear-cache

# Restart
echo "Restarting services..."
bench restart

echo ""
echo "=========================================="
echo "✅ HR Suite installed successfully!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Login to your site: http://$SITE_NAME"
echo "2. Navigate to HR Suite Dashboard"
echo "3. Start managing your HR operations!"
echo ""
echo "Documentation: https://github.com/macrobian88/hr_suite"
echo ""
