from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import Product

# Create your views here.

def members(request):
    template = loader.get_template('firsthtml.html')
    return HttpResponse(template.render())

def products(request):
    template = loader.get_template('list_products.html')
    products = Product.objects.all().values()
    context = {
        'products': products
    }
    return HttpResponse(template.render(request=request, ))
