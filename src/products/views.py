from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		context["title"] = "Class Based List"
		return context

def product_list_view(request):
	queryset = Product.objects.all()
	context = {
		"object_list": queryset,
		"title": "Function Based List",
	}
	return render(request, "products/product_list.html", context)

def product_list_index(request):
	queryset = Product.objects.all()
	paginator = Paginator(queryset, 6)
	page = request.GET.get('page')
	object_list = paginator.get_page(page)
	context = {
		"object_list": object_list,
		"title": "Index",
	}
	return render(request, "products/index.html", context)

class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = "products/detail.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		context["title"] = "Class Based Detail"
		return context

class FeaturedProductListView(ListView):
	template_name = "products/feature-list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		print(context)
		context["title"] = "Class Based Featured List"
		return context

	def get_queryset(self):
		qs = Product.objects.filter(featured=True)
		return qs

def product_list_search(request):
	q = request.GET.get('q', None)
	if q is None:
		queryset = Product.objects.all()
	else:
		queryset = Product.objects.filter(title__contains=q)
	paginator = Paginator(queryset, 6)
	page = request.GET.get('page')
	object_list = paginator.get_page(page)
	context = {
		"object_list": object_list,
		"title": "Index",
	}
	return render(request, "products/search.html", context)

	