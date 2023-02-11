from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class UpdateProfileForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ('name', 'about', 'date_of_birth', 'gender', 'linkedin_id', 
                'facebook_handle', 'twitter_handle', 'instagram_handle', 'website', 'country', 
                'state', 'profile_pic')
    
        widgets = {
                'name': forms.TextInput(attrs={'class':'form-control'}),
                'about':forms.Textarea(attrs={'class':'form-control', 'rows':'2'}),
                'date_of_birth': forms.widgets.DateInput(
                    format="%m/%d/%Y",
                    attrs={
                        'class':'form-control datetimepicker-input',
                        'data-target': '#datetimepicker1'}),
                'gender':forms.Select(attrs={'class':'form-control'}),
                'linkedin_id': forms.TextInput(attrs={'class':'form-control'}),
                'facebook_handle': forms.TextInput(attrs={'class':'form-control'}),
                'twitter_handle':forms.TextInput(attrs={'class':'form-control'}),
                'instagram_handle':forms.TextInput(attrs={'class':'form-control'}),
                'website':forms.TextInput(attrs={'class':'form-control'}),
                'country':forms.TextInput(attrs={'class':'form-control'}),
                'state':forms.TextInput(attrs={'class':'form-control'}),
                'profile_pic':forms.FileInput(attrs={'class':'form-control'})
        }

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2=forms.CharField(max_length=100, widget= forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

