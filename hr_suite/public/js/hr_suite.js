// HR Suite Custom JavaScript

frappe.ready(function() {
    // Custom JavaScript for HR Suite
    
    // Quick action handlers
    $(document).on('click', '.hr-quick-action-btn', function() {
        const action = $(this).data('action');
        handleQuickAction(action);
    });
});

function handleQuickAction(action) {
    switch(action) {
        case 'new_employee':
            frappe.new_doc('Employee');
            break;
        case 'leave_application':
            frappe.new_doc('Leave Application');
            break;
        case 'attendance':
            frappe.set_route('List', 'Attendance', 'Calendar');
            break;
        case 'payroll':
            frappe.set_route('List', 'Salary Slip');
            break;
        default:
            frappe.msgprint('Action not configured');
    }
}

// Auto-refresh dashboard stats
function refreshDashboardStats() {
    frappe.call({
        method: 'hr_suite.hr_suite.page.hr_suite_dashboard.hr_suite_dashboard.get_hr_stats',
        callback: function(r) {
            if (r.message) {
                updateDashboardUI(r.message);
            }
        }
    });
}

function updateDashboardUI(stats) {
    $('#total-employees').text(stats.total_employees);
    $('#on-leave-today').text(stats.on_leave_today);
    $('#pending-applications').text(stats.pending_leave_applications);
    $('#new-joinings').text(stats.new_joinings_this_month);
}

// Refresh stats every 5 minutes
setInterval(refreshDashboardStats, 300000);