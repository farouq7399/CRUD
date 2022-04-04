from django.shortcuts import render, redirect, reverse
from .models import product
from .forms import ProductForm
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from .serializers import productSerializer


class ProductList(ListView):
    template_name = 'home_page.html'
    queryset = product.objects.all()
    context_object_name = 'products'


class CreateProduct(CreateView):
    template_name = 'create_product.html'
    form_class = ProductForm
    context_object_name = "product"
    serializer_class = productSerializer

    def get_success_url(self):
        return reverse("list")


class detailsProduct(LoginRequiredMixin, DetailView):
    template_name = 'details_product.html'
    queryset = product.objects.all()
    context_object_name = 'product'

class DeleteProduct (DeleteView):
    template_name = 'delete_product.html'
    queryset = product.objects.all()

    def get_success_url(self):
        return redirect('list')



class LandingPageView(TemplateView):
    template_name ='landing.html'

