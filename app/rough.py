# import libraries
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

import json
from datetime import date


endpoint = os.environ.get('Azure_endpoint')
key = os.environ.get('Azure_key')

# def format_bounding_region(bounding_regions):
#     if not bounding_regions:
#         return "N/A"
#     return ", ".join("Page #{}: {}".format(region.page_number, format_polygon(region.polygon)) for region in bounding_regions)

# def format_polygon(polygon):
#     if not polygon:
#         return "N/A"
#     return ", ".join(["[{}, {}]".format(p.x, p.y) for p in polygon])



def analyze_invoice(invoiceUrl):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_analysis_client.begin_analyze_document_from_url(
        "prebuilt-invoice", invoiceUrl)
    invoices = poller.result()

    results = []

    for idx, invoice in enumerate(invoices.documents):
        print("--------Recognizing invoice #{}--------".format(idx + 1))

        vendor_name = invoice.fields.get("VendorName")
        if vendor_name:
            results.append(("Vendor Name", vendor_name))
            
            
        customer_name = invoice.fields.get("CustomerName")
        if customer_name:
            results.append(("Customer Name", customer_name))
            
            
        customer_id = invoice.fields.get("CustomerId")
        if customer_id:
            results.append(("Customer ID", customer_id))
            

        invoice_id = invoice.fields.get("InvoiceId")
        if invoice_id:
            results.append(("Invoice ID", invoice_id))
            
        
        invoice_date = invoice.fields.get("InvoiceDate")
        if invoice_date:
            results.append(("Invoice Date", invoice_date))
            
            
        invoice_total = invoice.fields.get("InvoiceTotal")
        if invoice_total:
            results.append(("Invoice Total", invoice_total))
            
            
        due_date = invoice.fields.get("DueDate")
        if due_date:
            results.append(("Due Date", due_date))
            
            
        purchase_order = invoice.fields.get("PurchaseOrder")
        if purchase_order:
            results.append(("Purchase Order", purchase_order))
                    

    return results

if __name__ == "__main__":
    link = '{{url}}'
    results = analyze_invoice(link)

    for label, result in results:
        print("{}: {}".format(label, result.value))
        