import frappe
import json

def create_workspaces():
    workspaces = [
        {
            "doctype": "Workspace",
            "name": "Manager Workspace",
            "label": "Manager Workspace",
            "title": "Manager Workspace",
            "icon": "file-manager",
            "public": 1,
            "module": "Custom Workspaces",
            "roles": [{"role": "System Manager"}],
            "links": [
                {"type": "Card Break", "label": "Users"},
                {"type": "Link", "label": "User", "link_type": "DocType", "link_to": "User"},
                {"type": "Link", "label": "Role", "link_type": "DocType", "link_to": "Role"}
            ],
            "shortcuts": [
                {"label": "Role Profile", "type": "DocType", "link_to": "Role Profile"}
            ],
            "quick_lists": [
                {"label": "Activity Log", "document_type": "Activity Log"}
            ],
            "content": json.dumps([
                {"id": "manager_header", "type": "header", "data": {"text": "<span class=\"h4\"><b>Manager Dashboard</b></span>", "col": 12}},
                {"id": "manager_shortcut", "type": "shortcut", "data": {"shortcut_name": "Role Profile", "col": 3}},
                {"id": "manager_card", "type": "card", "data": {"card_name": "Users", "col": 4}},
                {"id": "manager_ql", "type": "quick_list", "data": {"list_name": "Activity Log", "col": 12}}
            ])
        },
        {
            "doctype": "Workspace",
            "name": "Sales Workspace",
            "label": "Sales Workspace",
            "title": "Sales Workspace",
            "icon": "rupee",
            "public": 1,
            "module": "Custom Workspaces",
            "roles": [{"role": "Sales User"}, {"role": "Sales Manager"}],
            "links": [
                {"type": "Card Break", "label": "Selling"},
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
                {"id": "sales_header", "type": "header", "data": {"text": "<span class=\"h4\"><b>Sales Dashboard</b></span>", "col": 12}},
                {"id": "sales_shortcut", "type": "shortcut", "data": {"shortcut_name": "New Sales Order", "col": 3}},
                {"id": "sales_card", "type": "card", "data": {"card_name": "Selling", "col": 4}},
                {"id": "sales_ql", "type": "quick_list", "data": {"list_name": "Recent Customers", "col": 12}}
            ])
        },
        {
            "doctype": "Workspace",
            "name": "Operations Workspace",
            "label": "Operations Workspace",
            "title": "Operations Workspace",
            "icon": "truck",
            "public": 1,
            "module": "Custom Workspaces",
            "roles": [{"role": "Projects User"}, {"role": "System Manager"}],
            "links": [
                {"type": "Card Break", "label": "Operations"},
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
                {"id": "ops_header", "type": "header", "data": {"text": "<span class=\"h4\"><b>Operations Dashboard</b></span>", "col": 12}},
                {"id": "ops_shortcut", "type": "shortcut", "data": {"shortcut_name": "New Task", "col": 3}},
                {"id": "ops_card", "type": "card", "data": {"card_name": "Operations", "col": 4}},
                {"id": "ops_ql", "type": "quick_list", "data": {"list_name": "Active Projects", "col": 12}}
            ])
        }
    ]

    for ws in workspaces:
        if not frappe.db.exists("Workspace", ws["name"]):
            doc = frappe.get_doc(ws)
            doc.insert(ignore_permissions=True)
            
    frappe.db.commit()

def after_migrate():
    create_workspaces()

def before_uninstall():
    # Clean up the exact workspaces we generated
    workspaces = ["Manager Workspace", "Sales Workspace", "Operations Workspace"]
    for ws in workspaces:
        if frappe.db.exists("Workspace", ws):
            frappe.delete_doc("Workspace", ws, ignore_permissions=True)
