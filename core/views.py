from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import Certificate
from django.shortcuts import get_object_or_404

from .utils import render_to_pdf
from django.http import HttpResponse



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
    cert_details = Certificate.objects.get(certificate_number=id)
    context = {'data':cert_details}
    pdf = render_to_pdf('core/temp.html', context)
    return HttpResponse(pdf, content_type='application/pdf')


def verify_certificate(request):
    return render(request, 'core/verify_certificate.html', {})

def verify(request, id):
    cert_details = get_object_or_404(Certificate, certificate_number=id)
    context = {'data':cert_details}
    
    return render (request, 'core/verify.html', context)