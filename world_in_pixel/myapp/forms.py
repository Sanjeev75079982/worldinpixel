from django import forms
from django.contrib.auth.models import User
from myapp.models import UserForm, Contact
# Creating userform 

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')


class ContactForm(forms.ModelForm):
	
	class Meta:
		model = Contact
		fields = ('full_name', 'email','subject','description')


			





