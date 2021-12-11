from typing import List
from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    )

from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from produtos.models import Category, Product
 
@login_required
def index(request):
    return HttpResponse('Olá Django! (index)')

def ola(request):
    return HttpResponse('Olá, Django!')


class CreateCategoryView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ('name', 'description')
    template_name = 'create_category.html'
    success_url = reverse_lazy('list_category')

class ListCategoryView(ListView):
    model = Category
    template_name = 'list_category.html'
    context_object_name = 'categories'

class CreateProductView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'value', 'section', 'description')
    template_name = 'create_product.html'

class DetailCategoryView(DetailView):
    model = Category
    template_name = 'category_detail.html'
    #context_object_name = 'category'

class UpdateCategoryView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'category_form.html'
    fields = ('name', 'description')
    success_url = reverse_lazy('list_category')

class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_confirm_delete.html'
    success_url = reverse_lazy('list_category')


    