from django.shortcuts import render
from django.views import generic

from .models import Supplier, Product





class Product_List(generic.ListView):
    model = Product
    template_name = 'inventory/product_list.html'
    context_object_name = 'queryset'


def product_detail(request,id):
    product = Product.objects.get(pk=id)

    context = {'product': product,}
                
    return render(request,'inventory/product_detail.html',context)




    