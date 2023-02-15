from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ('profile_photo', 'certificate_number', 'name','role','organization', 'organizer','start_date', 'end_date')

        widgets = {
            # 'profile_photo': forms.FileField(attrs={'class':'form-control'}),
            'certificate_number': forms.TextInput(attrs={'class':'form-control'}),
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'role': forms.TextInput(attrs={'class':'form-control'}),
            'organization': forms.TextInput(attrs={'class':'form-control'}),
            'organizer': forms.TextInput(attrs={'class':'form-control'}),
            'organization': forms.TextInput(attrs={'class':'form-control'}),
    


        }