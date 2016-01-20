from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.detail import DetailView
from django.views.generic import View, TemplateView
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.db.models import Q
from django.utils import timezone
from .forms import VariationInventoryFormSet, ProductModelForm
from django.contrib import messages
from .mixins import StaffRequiredMixin, LoginRequiredMixin, MultiSlugMixin, SubmitMixin
import json
# Create your views here.

from .models import Product, Variation, Category

class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()
	template_name = "products/product_list.html"

class CategoryDetailView(DetailView):
	model = Category

	def get_context_data(self, *args, **kwargs):
		context = super(CategoryDetailView, self).get_context_data(*args, **kwargs)
		obj = self.get_object()
		product_set = obj.product_set.all()
		default_products = obj.default_category.all()
		products = (product_set | default_products).distinct() #combines default category
		context["products"] = products
		return context

class VariationListView(StaffRequiredMixin, ListView):
	model = Variation
	queryset = Variation.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(VariationListView, self).get_context_data(*args, **kwargs)
		context["formset"] = VariationInventoryFormSet(queryset=self.get_queryset())
		return context

	def get_queryset(self, *args, **kwargs):
		product_pk = self.kwargs.get("pk")
		if product_pk:
			product = get_object_or_404(Product, pk=product_pk)
			queryset = Variation.objects.filter(product=product)
		return queryset

	def post(self, request, *args, **kwargs):
		#
		formset = VariationInventoryFormSet(request.POST, request.FILES)
		print request.POST
		if formset.is_valid():
			formset.save(commit=False)
			for form in formset:
				new_item = form.save(commit=False)
				if new_item.title:								
					product_pk = self.kwargs.get("pk")						
					product = get_object_or_404(Product, pk=product_pk)
					new_item.product = product	
					new_item.save()		
				
			messages.success(request, "Your inventory and pricing has been updated.")
			return redirect("products")
		raise Http404

class ProductListView(ListView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super(ProductListView, self).get_context_data(*args, **kwargs)
		context["now"] = timezone.now()
		context["query"] = self.request.GET.get("q") #none
		return context

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_queryset(*args, **kwargs)
		query = self.request.GET.get("q")
		if query: #searches for title, desc, price
			qs = self.model.objects.filter(
				Q(title__icontains=query) |
				Q(description__icontains=query)
				)
			try:
				qs2 = self.model.objects.filter(
				Q(price=query)
				)
				qs = (qs | qs2).distinct()
			except:
				pass
		return qs

class ProductAddView(SubmitMixin, CreateView):
	model = Product
	form_class = ProductModelForm
	template_name = "products/form.html"
	success_url = "/products/add"
	submit_btn = "Submit"
	title = "Submit"

class ProductUpdateView(SubmitMixin, MultiSlugMixin, UpdateView):
	model = Product
	form_class = ProductModelForm
	template_name = "products/form.html"
	success_url = "/products/"
	submit_btn = "Update"
	title = "Update"

class ProductDetailView(MultiSlugMixin, DetailView):
	model = Product
	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		context["related"] = Product.objects.get_related(instance)
		return context

def product_detail_view_func(request, id):
	product_instance = get_object_or_404(Product, id=id)

	try:
		product_instance = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404
	except:
		raise Http404

	template = "products/product_detail.html"
	context = {
		"object": product_instance
	}
	return render(request, template, context)

def create_view(request):
	model = Product
	def get_queryset(self, *args, **kwargs):
		qs = super(ProductListView, self).get_context_data(**kwargs)
		return qs
	form = ProductModelForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		messages.success(request, "Your Question has been saved.")
		# data = form.cleaned_data
		# title = data.get("title")
		# description = data.get("description")
		# #price = data.get("price")
		# new_obj = Product.objects.create(title=title, description=description)
	template = "products/create_view.html"
	context = {
		"form": form,
	}
	return render(request, template, context)

def edit_view(request, object_id=None):					
	product = get_object_or_404(Product, id=object_id)
	form = ProductModelForm(request.POST or None, instance=Product)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Your Question has been saved.")
		# data = form.cleaned_data
		# title = data.get("title")
		# description = data.get("description")
		# #price = data.get("price")
		# new_obj = Product.objects.create(title=title, description=description)
	template = "products/update_view.html"
	context = {
		"form": form,
		"object": product,
	}
	return render(request, template, context)

def detail_slug_view(request, slug=None):
	product = Product.objects.get(slug=slug)
	try:
		product = get_object_or_404(Product, slug=slug)
	except Product.MultipleObjectsReturned:
		product = Product.objects.filter(slug=slug).order_by("-title").first()
		template = "products/product_detail.html"
		context = {
			"object": product
		}
		return render(request, template, context)

class ExampleView(TemplateView):
    template_name = "products/example.html"

    def get_context_data(self, **kwargs):
        context = super(ExampleView, self).get_context_data(**kwargs)
        if self.request.GET.get('id'):
	        example = Example.objects.get(id=self.request.GET.get["id"]).all()
	       	context["title"] = example.title
	       	context["content"] = example.content
	       	context["link"] = example.link
       	else:
       		print "no example"
        return context