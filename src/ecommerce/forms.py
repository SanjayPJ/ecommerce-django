from django import forms

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