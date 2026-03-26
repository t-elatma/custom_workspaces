app_name = "custom_workspaces"
app_title = "Custom Workspaces"
app_publisher = "Custom App Author"
app_description = "A custom Frappe app to auto-generate workspaces"
app_email = "author@example.com"
app_license = "mit"

# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
app_include_css = "/assets/custom_workspaces/css/workspace.css"
# app_include_js = "/assets/custom_app/js/custom_app.js"

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

after_migrate = "custom_workspaces.install.after_migrate"
after_install = "custom_workspaces.install.after_migrate"
before_uninstall = "custom_workspaces.install.before_uninstall"
