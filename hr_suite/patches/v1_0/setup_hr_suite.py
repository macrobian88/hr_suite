import frappe

def execute():
    """
    Patch to setup HR Suite after installation
    """
    # This ensures setup runs even if after_install wasn't called
    from hr_suite.install import after_install
    
    try:
        after_install()
    except Exception as e:
        frappe.log_error(f"HR Suite Setup Error: {str(e)}")