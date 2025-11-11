frappe.pages['hr-suite-dashboard'].on_page_load = function(wrapper) {
    var page = frappe.ui.make_app_page({
        parent: wrapper,
        title: 'HR Suite Dashboard',
        single_column: true
    });
    
    // Add refresh button
    page.add_button('Refresh', function() {
        loadDashboard();
    }, 'octicon octicon-sync');
    
    loadDashboard();
    
    function loadDashboard() {
        frappe.call({
            method: 'hr_suite.hr_suite_dashboard.page.hr_suite_dashboard.hr_suite_dashboard.get_hr_stats',
            callback: function(r) {
                if (r.message) {
                    renderDashboard(page, r.message);
                }
            }
        });
    }
    
    function renderDashboard(page, stats) {
        let html = `
            <div class="hr-suite-dashboard">
                <div class="row">
                    <div class="col-md-3">
                        <div class="hr-stat-card">
                            <h3>Total Employees</h3>
                            <div class="stat-value" id="total-employees">${stats.total_employees}</div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="hr-stat-card">
                            <h3>On Leave Today</h3>
                            <div class="stat-value" id="on-leave-today">${stats.on_leave_today}</div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="hr-stat-card">
                            <h3>Pending Applications</h3>
                            <div class="stat-value" id="pending-applications">${stats.pending_leave_applications}</div>
                        </div>
                    </div>
                    <div class="col-md-3">
                        <div class="hr-stat-card">
                            <h3>New Joinings (This Month)</h3>
                            <div class="stat-value" id="new-joinings">${stats.new_joinings_this_month}</div>
                        </div>
                    </div>
                </div>
                
                <div class="row">
                    <div class="col-md-12">
                        <h3>Quick Actions</h3>
                        <div class="hr-quick-actions">
                            <div class="hr-quick-action-btn" data-action="new_employee">
                                <i class="octicon octicon-person"></i> Add New Employee
                            </div>
                            <div class="hr-quick-action-btn" data-action="leave_application">
                                <i class="octicon octicon-calendar"></i> New Leave Application
                            </div>
                            <div class="hr-quick-action-btn" data-action="attendance">
                                <i class="octicon octicon-checklist"></i> Mark Attendance
                            </div>
                            <div class="hr-quick-action-btn" data-action="payroll">
                                <i class="octicon octicon-credit-card"></i> Process Payroll
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        $(page.body).html(html);
    }
}