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
            "content": json.dumps([
                {"id": "manager_header", "type": "header", "data": {"text": "<span class=\"h4\"><b>Manager Dashboard</b></span>", "col": 12}},
                {"id": "manager_card", "type": "card", "data": {"card_name": "Users", "col": 4}}
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
            "content": json.dumps([
                {"id": "sales_header", "type": "header", "data": {"text": "<span class=\"h4\"><b>Sales Dashboard</b></span>", "col": 12}},
                {"id": "sales_card", "type": "card", "data": {"card_name": "Selling", "col": 4}}
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
            "content": json.dumps([
                {"id": "ops_header", "type": "header", "data": {"text": "<span class=\"h4\"><b>Operations Dashboard</b></span>", "col": 12}},
                {"id": "ops_card", "type": "card", "data": {"card_name": "Operations", "col": 4}}
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
