from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html', {})

def certificate_detail(request):
    return render (request, 'core/certificate_detail.html', {})