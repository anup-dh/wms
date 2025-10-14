import frappe

@frappe.whitelist()
def submitDoc(doctype, docname):
    try:
        doc = frappe.get_doc(doctype, docname)
        if doc.docstatus == 0:
            doc.submit()
            # This line is absolutely essential!
            frappe.db.commit() 
            frappe.response.message = f"Successfully submitted {docname}"
        else:
            frappe.response.message = f"{docname} was not in a draft state."
    except Exception as e:
        frappe.log_error(title='Submission Failed', message=frappe.get_traceback())
        # Send a clear error back to the user
        frappe.throw(f"An error occurred during submission: {e}")