import frappe
import json

def create_dependencies():
    # 1. Custom HTML Block
    if not frappe.db.exists("Custom HTML Block", "Workspace Guide"):
        frappe.get_doc({
            "doctype": "Custom HTML Block",
            "name": "Workspace Guide",
            "private": 0,
            "html": "<div style='padding: 20px; background: var(--bg-light-gray); border-radius: 8px;'><h3 class='text-muted'>🚀 Advanced Capabilities Activated</h3><p>Enjoy widgets, charts, and more generated directly via python.</p></div>"
        }).insert(ignore_permissions=True)

    # 2. Number Card
    if not frappe.db.exists("Number Card", "Total Users"):
        frappe.get_doc({
            "doctype": "Number Card",
            "name": "Total Users",
            "label": "Total Users",
            "document_type": "User",
            "function": "Count",
            "is_standard": 1,
            "show_percentage_stats": 0
        }).insert(ignore_permissions=True)

    # 3. Dashboard Chart
    if not frappe.db.exists("Dashboard Chart", "Users Chart"):
        frappe.get_doc({
            "doctype": "Dashboard Chart",
            "name": "Users Chart",
            "chart_name": "Users Chart",
            "chart_type": "Line",
            "document_type": "User",
            "based_on": "creation",
            "time_interval": "Monthly",
            "timeseries": 1,
            "is_standard": 1
        }).insert(ignore_permissions=True)

    # 4. Module Onboarding
    if not frappe.db.exists("Module Onboarding", "Custom App Onboarding"):
        frappe.get_doc({
            "doctype": "Module Onboarding",
            "name": "Custom App Onboarding",
            "title": "Welcome to Custom App",
            "subtitle": "Let's get started",
            "success_message": "All done!",
            "is_complete": 0
        }).insert(ignore_permissions=True)

def create_workspaces():
    create_dependencies()

    workspaces = [
        {
            "doctype": "Workspace",
            "name": "Manager Workspace",
            "label": "Manager Workspace",
            "title": "Manager Workspace",
            "icon": "users",
            "indicator_color": "blue",
            "public": 1,
            "module": "Custom Workspaces",
            "roles": [{"role": "System Manager"}],
            "links": [
                {"type": "Card Break", "label": "Administration"},
                {"type": "Link", "label": "User", "link_type": "DocType", "link_to": "User"},
                {"type": "Link", "label": "Role", "link_type": "DocType", "link_to": "Role"}
            ],
            "shortcuts": [
                {"label": "Role Profile", "type": "DocType", "link_to": "Role Profile"}
            ],
            "quick_lists": [
                {"label": "Recent Users", "document_type": "User"}
            ],
            "charts": [
                {"label": "Users Chart", "chart_name": "Users Chart"}
            ],
            "number_cards": [
                {"label": "Total Users", "number_card_name": "Total Users"}
            ],
            "custom_blocks": [
                {"label": "Workspace Guide", "custom_block_name": "Workspace Guide"}
            ],
            "content": json.dumps([
                {"id": "mgr_h1", "type": "header", "data": {"text": "<span class=\"h4\"><b>Premium Manager Dashboard</b></span>", "col": 12}},
                {"id": "mgr_t1", "type": "text", "data": {"text": "<p>This layout uses almost every dashboard component available in Frappe!</p>", "col": 12}},
                {"id": "mgr_cb", "type": "custom_block", "data": {"custom_block_name": "Workspace Guide", "col": 12}},
                {"id": "mgr_sp", "type": "spacer", "data": {"col": 12}},
                {"id": "mgr_nc", "type": "number_card", "data": {"number_card_name": "Total Users", "col": 4}},
                {"id": "mgr_sc", "type": "shortcut", "data": {"shortcut_name": "Role Profile", "col": 4}},
                {"id": "mgr_ch", "type": "chart", "data": {"chart_name": "Users Chart", "col": 12}},
                {"id": "mgr_cd", "type": "card", "data": {"card_name": "Administration", "col": 4}},
                {"id": "mgr_ql", "type": "quick_list", "data": {"list_name": "Recent Users", "col": 12}}
            ])
        },
        {
            "doctype": "Workspace",
            "name": "Sales Workspace",
            "label": "Sales Workspace",
            "title": "Sales Workspace",
            "icon": "rupee",
            "indicator_color": "green",
            "public": 1,
            "module": "Custom Workspaces",
            "roles": [{"role": "Sales User"}, {"role": "Sales Manager"}],
            "links": [
                {"type": "Card Break", "label": "Sales Data"},
                {"type": "Link", "label": "Customer", "link_type": "DocType", "link_to": "Customer"},
                {"type": "Link", "label": "Sales Order", "link_type": "DocType", "link_to": "Sales Order"}
            ],
            "shortcuts": [
                {"label": "New Sales Order", "type": "DocType", "link_to": "Sales Order"}
            ],
            "quick_lists": [
                {"label": "Recent Customers", "document_type": "Customer"}
            ],
            "content": json.dumps([
                {"id": "sls_h1", "type": "header", "data": {"text": "<span class=\"h4\"><b>Sales Command Center</b></span>", "col": 12}},
                {"id": "sls_o1", "type": "onboarding", "data": {"onboarding_name": "Custom App Onboarding", "col": 12}},
                {"id": "sls_sc", "type": "shortcut", "data": {"shortcut_name": "New Sales Order", "col": 4}},
                {"id": "sls_cd", "type": "card", "data": {"card_name": "Sales Data", "col": 4}},
                {"id": "sls_ql", "type": "quick_list", "data": {"list_name": "Recent Customers", "col": 12}}
            ])
        },
        {
            "doctype": "Workspace",
            "name": "Operations Workspace",
            "label": "Operations Workspace",
            "title": "Operations Workspace",
            "icon": "truck",
            "indicator_color": "orange",
            "public": 1,
            "module": "Custom Workspaces",
            "roles": [{"role": "Projects User"}, {"role": "System Manager"}],
            "links": [
                {"type": "Card Break", "label": "Operations Board"},
                {"type": "Link", "label": "Project", "link_type": "DocType", "link_to": "Project"},
                {"type": "Link", "label": "Task", "link_type": "DocType", "link_to": "Task"}
            ],
            "shortcuts": [
                {"label": "New Task", "type": "DocType", "link_to": "Task"}
            ],
            "quick_lists": [
                {"label": "Active Projects", "document_type": "Project"}
            ],
            "content": json.dumps([
                {"id": "ops_h1", "type": "header", "data": {"text": "<span class=\"h4\"><b>Operations Dashboard</b></span>", "col": 12}},
                {"id": "ops_sc", "type": "shortcut", "data": {"shortcut_name": "New Task", "col": 4}},
                {"id": "ops_cd", "type": "card", "data": {"card_name": "Operations Board", "col": 4}},
                {"id": "ops_ql", "type": "quick_list", "data": {"list_name": "Active Projects", "col": 12}}
            ])
        }
    ]

    for ws in workspaces:
        if not frappe.db.exists("Workspace", ws["name"]):
            frappe.get_doc(ws).insert(ignore_permissions=True)
        else:
            # Update existing workspace to ensure our new layout applies
            doc = frappe.get_doc("Workspace", ws["name"])
            doc.update(ws)
            doc.save(ignore_permissions=True)
            
    frappe.db.commit()

def after_migrate():
    create_workspaces()

def before_uninstall():
    # Clean up the exact workspaces we generated
    workspaces = ["Manager Workspace", "Sales Workspace", "Operations Workspace"]
    for ws in workspaces:
        if frappe.db.exists("Workspace", ws):
            frappe.delete_doc("Workspace", ws, ignore_permissions=True)
            
    docs_to_delete = [
        ("Custom HTML Block", "Workspace Guide"),
        ("Number Card", "Total Users"),
        ("Dashboard Chart", "Users Chart"),
        ("Module Onboarding", "Custom App Onboarding")
    ]
    for dt, dn in docs_to_delete:
        if frappe.db.exists(dt, dn):
            frappe.delete_doc(dt, dn, ignore_permissions=True)
