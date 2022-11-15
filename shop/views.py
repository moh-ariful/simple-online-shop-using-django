from django.shortcuts import render
from .models import Products

def index(request):
    product_objects = Products.objects.all()
    context = {
        'product_objects': product_objects,
    }
    return render(request, 'shop/index.html', context)