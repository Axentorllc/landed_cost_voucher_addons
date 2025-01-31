app_name = "landed_cost_voucher_addons"
app_title = "Landed Cost Voucher Addons"
app_publisher = "Axentor LLC"
app_description = "Landed Cost Voucher Addons on ERPNext"
app_email = "apps@axentor.co"
app_license = "gpl-3.0"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "landed_cost_voucher_addons",
# 		"logo": "/assets/landed_cost_voucher_addons/logo.png",
# 		"title": "Landed Cost Voucher Addons",
# 		"route": "/landed_cost_voucher_addons",
# 		"has_permission": "landed_cost_voucher_addons.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/landed_cost_voucher_addons/css/landed_cost_voucher_addons.css"
# app_include_js = "/assets/landed_cost_voucher_addons/js/landed_cost_voucher_addons.js"

# include js, css files in header of web template
# web_include_css = "/assets/landed_cost_voucher_addons/css/landed_cost_voucher_addons.css"
# web_include_js = "/assets/landed_cost_voucher_addons/js/landed_cost_voucher_addons.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "landed_cost_voucher_addons/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Landed Cost Voucher": "public/js/landed_cost_voucher.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "landed_cost_voucher_addons/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "landed_cost_voucher_addons.utils.jinja_methods",
# 	"filters": "landed_cost_voucher_addons.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "landed_cost_voucher_addons.install.before_install"
# after_install = "landed_cost_voucher_addons.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "landed_cost_voucher_addons.uninstall.before_uninstall"
# after_uninstall = "landed_cost_voucher_addons.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "landed_cost_voucher_addons.utils.before_app_install"
# after_app_install = "landed_cost_voucher_addons.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "landed_cost_voucher_addons.utils.before_app_uninstall"
# after_app_uninstall = "landed_cost_voucher_addons.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "landed_cost_voucher_addons.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Landed Cost Voucher": {
        "on_submit": "landed_cost_voucher_addons.custom_hooks.landed_cost.on_submit",
        "on_cancel": "landed_cost_voucher_addons.custom_hooks.landed_cost.on_cancel",
        "before_save": "landed_cost_voucher_addons.custom_hooks.landed_cost.sum_invoice_and_charges",
    },
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"landed_cost_voucher_addons.tasks.all"
# 	],
# 	"daily": [
# 		"landed_cost_voucher_addons.tasks.daily"
# 	],
# 	"hourly": [
# 		"landed_cost_voucher_addons.tasks.hourly"
# 	],
# 	"weekly": [
# 		"landed_cost_voucher_addons.tasks.weekly"
# 	],
# 	"monthly": [
# 		"landed_cost_voucher_addons.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "landed_cost_voucher_addons.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "landed_cost_voucher_addons.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "landed_cost_voucher_addons.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["landed_cost_voucher_addons.utils.before_request"]
# after_request = ["landed_cost_voucher_addons.utils.after_request"]

# Job Events
# ----------
# before_job = ["landed_cost_voucher_addons.utils.before_job"]
# after_job = ["landed_cost_voucher_addons.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"landed_cost_voucher_addons.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                    "Landed Cost Taxes and Charges-party_type",
                    "Landed Cost Taxes and Charges-party",
                    "Landed Cost Taxes and Charges-is_paid",
                    "Landed Cost Taxes and Charges-paid_from_account",
                    "Landed Cost Voucher-sum_invoice_and_charges",
                    "Landed Cost Voucher-journal_entry",
                ],
            ]
        ],
    }
]
