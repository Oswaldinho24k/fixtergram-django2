from django import forms
from django.contrib.auth.models import User
from .models import Profile



class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude =['user']

class UserRegistrationForm(forms.ModelForm):
 	password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
 	password2 = forms.CharField(label='Repite la Contraseña', widget=forms.PasswordInput())
 	username = forms.CharField(label='Nombre de Usuario', widget=forms.TextInput())
 	email = forms.EmailField(label='Email', widget=forms.EmailInput())

 	class Meta:
 		model = User
 		fields = ('username', 'email')

 	def clean_password2(self):
 		cd = self.cleaned_data
 		if cd['password'] != cd['password2']:
 			raise forms.ValidationError('Las contraseñas no coinciden')
 		return cd['password2']




 