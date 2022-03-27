from django.shortcuts import render, redirect, reverse
from .models import product
from .forms import ProductForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductList( ListView):
    template_name = 'home_page.html'
    queryset = product.objects.all()
    context_object_name = 'products'

class UsersList(ListView):
    template_name = 'home_page.html'
    queryset = User.objects.all()
    context_object_name = 'products'


class CreateProduct(CreateView):
    template_name = 'create_product.html'
    form_class = ProductForm
    context_object_name = "product"
