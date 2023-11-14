# import libraries
import os
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

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

        invoice_id = invoice.fields.get("InvoiceId")
        if invoice_id:
            results.append(("Invoice ID", invoice_id))

    return results

if __name__ == "__main__":
    link = '{{url}}'
    results = analyze_invoice(link)

    for label, result in results:
        print("{}: {}".format(label, result.value))

    print("----------------------------------------")

    
    
            #     print(
            #     "Vendor Name: {} has confidence: {}".format(
            #         vendor_name.value, vendor_name.confidence
            #     )
            # )