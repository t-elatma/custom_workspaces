import frappe
import json

def create_dependencies():
    # 1. Custom HTML Block
    if not frappe.db.exists("Custom HTML Block", "Workspace Guide"):
        frappe.get_doc({
            "doctype": "Custom HTML Block",
            "name": "Workspace Guide",
            "private": 0,
            "html": "<div style='position: relative; overflow: hidden; padding: 40px; border-radius: 20px; background: linear-gradient(135deg, #4f46e5 0%, #ec4899 100%); color: white; box-shadow: 0 10px 25px -5px rgba(236, 72, 153, 0.4);'><div style='position: relative; z-index: 2;'><h2 style='font-weight: 800; margin-bottom: 10px; font-size: 28px; line-height: 1.2;'>✨ Premium Workspace Experience</h2><p style='font-size: 16px; opacity: 0.9; max-width: 600px; margin: 0;'>This workspace employs advanced custom HTML wrappers and injected desk CSS to deliver a uniquely elegant and colorful design.</p></div><div style='position: absolute; top: -50px; right: -50px; width: 200px; height: 200px; background: rgba(255,255,255,0.1); border-radius: 50%; filter: blur(20px);'></div><div style='position: absolute; bottom: -80px; left: 20%; width: 250px; height: 250px; background: rgba(255,255,255,0.15); border-radius: 50%; filter: blur(30px);'></div></div>"
        }).insert(ignore_permissions=True)

    # 2. Number Card
    if not frappe.db.exists("Number Card", "Total Users"):
        frappe.get_doc({
            "doctype": "Number Card",
            "name": "Total Users",
            "label": "Total Users",
            "document_type": "User",
            "function": "Count",
            "show_percentage_stats": 0
        }).insert(ignore_permissions=True)

    # 3. Dashboard Chart
    if not frappe.db.exists("Dashboard Chart", "Users Chart"):
        frappe.get_doc({
            "doctype": "Dashboard Chart",
            "name": "Users Chart",
            "chart_name": "Users Chart",
            "chart_type": "Count",
            "type": "Line",
            "document_type": "User",
            "based_on": "creation",
            "time_interval": "Monthly",
            "timeseries": 1,
            "filters_json": "{}"
        }).insert(ignore_permissions=True)

    # Module Onboarding removed to avoid strict validation errors

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
        ("Dashboard Chart", "Users Chart")
    ]
    for dt, dn in docs_to_delete:
        if frappe.db.exists(dt, dn):
            frappe.delete_doc(dt, dn, ignore_permissions=True)
