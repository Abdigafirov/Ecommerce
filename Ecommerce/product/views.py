from django.urls import reverse_lazy
from .models.product import Product
from .models.category import Category
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from .forms import ProductCreateForm, ProductForm
# Create your views here.


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'category'


class ProductDetailView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'




def ProductSavat(request):
    print(request.POST['inputname'])
    return render(request, 'savat.html')


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductCreateForm
    success_url = reverse_lazy('index')


class ProductDelete(DeleteView):
    model = Product
    template_name = 'delete.html'
    success_url = reverse_lazy('index')


class ProductEdit(UpdateView):
    model = Product
    template_name = 'edit.html'
    form_class = ProductForm
    success_url = reverse_lazy('index')
