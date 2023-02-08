from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group


# Create your views here.
def register(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context)
