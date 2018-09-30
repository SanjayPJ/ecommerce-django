from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class ContactForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	content = forms.CharField(widget=forms.Textarea())

	name.widget.attrs.update({"class": "form-control", "placeholder": "Enter Your Name"})
	email.widget.attrs.update({"class": "form-control", "placeholder": "Enter Your Email"})
	content.widget.attrs.update({"class": "form-control", "placeholder": "Enter Some Content Here"})

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if "gmail.com" not in email:
			raise forms.ValidationError("Email has to be gmail.com")
		return email

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

	username.widget.attrs.update({"class": "form-control"})
	password.widget.attrs.update({"class": "form-control"})

class RegisterForm(forms.Form):
	username = forms.CharField()
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput())

	username.widget.attrs.update({"class": "form-control"})
	email.widget.attrs.update({"class": "form-control"})
	password.widget.attrs.update({"class": "form-control"})
	password2.widget.attrs.update({"class": "form-control"})

	def clean_username(self):
		username = self.cleaned_data.get("username")
		qs = User.objects.filter(username=username)
		if qs.exists:
			raise forms.ValidationError("Username is taken")
		return username

	def clean_email(self):
		email = self.cleaned_data.get("email")
		qs = User.objects.filter(email=email)
		if qs.exists:
			raise forms.ValidationError("Email is taken")

	def clean(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if password2 != password:
			raise forms.ValidationError("Passwords Must Match")
		return self.cleaned_data