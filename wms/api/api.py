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

import frappe

@frappe.whitelist(allow_guest=True)
def getBinData(item_code):
    """
    Fetches all Bin records for a given item_code.
    """
    if not item_code:
        frappe.throw("Item Code is required.")

    # Define the filters to find the correct bins
    filters = {"item_code": item_code}

    # Use Frappe's ORM to get all matching records
    # The '*' returns all columns for each bin
    bin_records = frappe.get_all('Bin', filters=filters, fields=['*'])
    
    # Return the list of bin records
    return bin_records