from django.shortcuts import render
from .models import product as product_model

# Create your views here.


def product_view(request,pid):
    product = product_model.objects.get(id=pid)
    context = {
        'product' : product
    }
    product.visits += 1
    product.save()
    return render(request,'product.html',context)