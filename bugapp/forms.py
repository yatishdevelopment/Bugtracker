from django import forms
from bugapp.models import *



class User_form(forms.ModelForm):
	class Meta:
		model = User
		fields = ["user_name","password"]
		widgets = {
		"user_name":forms.TextInput(attrs={'class':'form-control','id':'id_name',}),	
		"password":forms.PasswordInput(attrs={'class':'form-control','id':'id_password'}),
		}