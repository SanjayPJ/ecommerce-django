from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
	context = {
		"title": "Index Page",
		"content": "Welcome to Index Page",
	}
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
