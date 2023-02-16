from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CertificateForm
from .models import Certificate

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
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        verification_link = f"http://127.0.0.1:8000/{cerificate_number}/verify"
        Certificate.objects.create(profile_photo=profile_photo, certificate_number = cerificate_number, name = name, role=role, organization=organization, organizer=organizer, start_date=start_date, end_date=end_date, verification_link=verification_link)
        
        return HttpResponseRedirect(reverse('certificate_detail', args=(cerificate_number)))

    return render(request, 'core/generate_certificate.html')
