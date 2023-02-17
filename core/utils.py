from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def render_to_pdf(template_path, context):
    # Load the template
    template = get_template(template_path)
    html = template.render(context)

    # Create a HttpResponse object with the PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="output.pdf"'

    # Create a PDF file using the HTML content
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('PDF generation failed', status=500)

    return response
