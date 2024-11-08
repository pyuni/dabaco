from django import forms
from .models import contactClass
class contactForm(forms.ModelForm):
    class Meta:
        model=contactClass
        fields=['firstname','lastname','email','msg']
        widgets={'firstname':forms.TextInput(attrs={'placeholder':"اسم"}),
                 'lastname':forms.TextInput(attrs={'placeholder':"فامیل"}),
                 'email':forms.TextInput(attrs={'placeholder':"ایمیل"}),
                 'msg':forms.Textarea(attrs={'placeholder':"پیام"})
                 
                 }