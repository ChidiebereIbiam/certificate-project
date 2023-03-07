from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Certificate
from django.shortcuts import get_object_or_404

from .utils import render_to_pdf


import os
from django.conf import settings
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.contrib import messages

def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
                result = [result]
        result = list(os.path.realpath(path) for path in result)
        path=result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
            raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
            )
    return path


# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {})

def certificate_detail(request, id):
    cert_details = Certificate.objects.get(certificate_number=id)
    context = {'data':cert_details}
    return render (request, 'core/certificate_detail.html', context)

def generate_certificate(request):
    if request.method == 'POST':
        profile_photo = request.FILES['profile_photo']
        cerificate_number = request.POST['certificate_number']
        name = request.POST['c_name']
        role = request.POST['role']
        organization = request.POST['organization']
        organizer = request.POST['organizer']
        internship_name = request.POST['internship_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        verification_link = f"http://127.0.0.1:8000/{cerificate_number}/verify"
        Certificate.objects.create(profile_photo=profile_photo, certificate_number = cerificate_number, name = name, role=role, organization=organization, organizer=organizer, internship_name = internship_name, start_date=start_date, end_date=end_date, verification_link=verification_link)

        return HttpResponseRedirect(reverse('manage_certificate'))

    return render(request, 'core/generate_certificate.html')

def manage_certificate(request):
    cert = Certificate.objects.all().order_by('-id').values()
    return render(request, 'core/manage_certificate.html', {'cert':cert})

def delete_certificate(request, id):
    certificate = Certificate.objects.get(id=id)
    certificate.delete()
    return HttpResponseRedirect(reverse('manage_certificate'))

def generate_pdf(request, id):
    # cert_details = Certificate.objects.get(certificate_number=id)
    # context = {'data':cert_details}
    # pdf = render_to_pdf('core/temp.html', context)
    # return HttpResponse(pdf, content_type='application/pdf')
    cert_details = Certificate.objects.get(certificate_number=id)
    context = {'data':cert_details, 'base':settings.BASE_DIR}
    print(context)
    pdf = render_to_pdf('core/temp.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type = 'application/pdf')
        filename = f"certificate-{id}.pdf"
        content = f"inline; filename={filename}"
        response['Content-Disposition'] = content
        return response
    return HttpResponse ('Error generating PDF')

def render_pdf_view(request, id):
    template_path = 'core/temp.html'
    cert_details = Certificate.objects.get(certificate_number=id)
    context = {'data':cert_details}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def verify_certificate(request):
    return render(request, 'core/verify_certificate.html', {})

def verify(request, id):
    context = {}
    try:
        cert_details = Certificate.objects.get(certificate_number=id)
        context = {'data':cert_details}
    except Certificate.DoesNotExist:
        print("Nothing")

    return render (request, 'core/verify.html', context)
