from frappe import _

def get_data():
    return [
        {
            "module_name": "HR Suite Dashboard",
            "category": "Modules",
            "label": _("HR Suite"),
            "color": "#FF5733",
            "icon": "octicon octicon-organization",
            "type": "module",
            "description": _("Complete HR Management Solution"),
            "onboard_present": 1
        }
    ]