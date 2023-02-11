from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, UpdateProfileForm,PasswordChangingForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import Group
from .models import Profile
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin



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

class ProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    
class UpdateProfileView(generic.UpdateView, LoginRequiredMixin):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('dashboard')


class PasswordsChangeView(PasswordChangeView, LoginRequiredMixin):
    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

@login_required
def Password_Success(request):
    return render (request, 'registration/password_success.html', {})


