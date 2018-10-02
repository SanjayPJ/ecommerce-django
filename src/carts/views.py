from django.shortcuts import render

# Create your views here.


def cart_home(request):
    request.session['user'] = request.user.username
    return render(request, 'carts/home.html', {})
