from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm

User = get_user_model()

def home_page(request):
	context = {
		"title": "Index Page",
		"content": "Welcome to Index Page",
	}
	if request.user.is_authenticated:
		context['premium_content'] = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ex, dolorum!"
	return render(request, "home_page.html", context)

def about_page(request):
	context = {
		"title": "About Page",
		"content": "Welcome to About Page",
	}
	return render(request, "home_page.html", context)

def contact_page(request):
	contact_form = ContactForm(request.POST or None)
	context = {
		"title": "Contact Page",
		"content": "Welcome to Contact Page",
		"form": contact_form,
	}
	if contact_form.is_valid():
		print(contact_form.cleaned_data)
		# print(contact_form.cleaned_data.get("name"))
		# print(contact_form.cleaned_data.get("email"))
		# print(contact_form.cleaned_data.get("content"))
	if request.method == "GET":
		# print all the get element
		print(request.GET)
		print(request.GET.get("name"))
	if request.method == "POST":
		# print the whole dict
		print(request.POST)
		# print each element
		# print(request.POST.get("name"))
		# print(request.POST.get("email"))
	return render(request, "contact/view.html", context)

def login_page(request):
	login_form = LoginForm(request.POST or None)
	context = {
		"form": login_form,
		"title": "Log In",
		"content": "Let's Log In"
	}
	if login_form.is_valid():
		# print(login_form.cleaned_data)
		username = login_form.cleaned_data.get("username")
		password = login_form.cleaned_data.get("password")
		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			# context["form"] = LoginForm()
			return redirect("admin:index")
		else:
			print("Error")

	return render(request, "auth/login.html", context)

def register_page(request):
	register_form = RegisterForm(request.POST or None)
	if register_form.is_valid():
		# print(register_form.cleaned_data)
		username = register_form.cleaned_data.get("username")
		email = register_form.cleaned_data.get("email")
		password = register_form.cleaned_data.get("password")
		# print(username, email, password)
		user = User.objects.create_user(username, email, password)
		user.save()
		return redirect("login")
	context = {
		"title": "Register",
		"content": "Waiting for something?",
		"form": register_form,
	}
	return render(request, "auth/register.html", context)

def home_page_old1(request):
	html_ = """
	<!doctype html>
	<html lang="en">
	  <head>
	    <!-- Required meta tags -->
	    <meta charset="utf-8">
	    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

	    <!-- Bootstrap CSS -->
	    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">

	    <title>Hello, world!</title>
	  </head>
	  <body>
	    <h1>Hello, world!</h1>

	    <!-- Optional JavaScript -->
	    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
	    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
	    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
	    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
	  </body>
	</html>
	"""
	return HttpResponse(html_)

def home_page_old(request):
	return HttpResponse("Hello World!")
