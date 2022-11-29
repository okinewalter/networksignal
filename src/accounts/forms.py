from django import forms
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth import get_user_model 
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = get_user_model()
        fields = ['new_password1', 'new_password2']


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	password1 = forms.CharField(label='Enter password',
								widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirm password',
								widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		help_texts = {
			'username': None,
			'email': None,
			'password1': None,
			'password2': None,
		}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user