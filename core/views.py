from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CertificateForm
from .models import Certificate

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {})

def certificate_detail(request):
    return render (request, 'core/certificate_detail.html', {})

def generate_certificate(request):
    if request.method == 'POST':
        cerificate_number = request.POST['certificate_number']
    return render(request, 'core/generate_certificate.html')
