from django.shortcuts import render

from . models import Category, Product

# Create your views here.

def store (request):
    all_products = Product.objects.all() #getting hold of all the products

    context = {'all_products':all_products}

    return render(request,'store/store.html', context)

def categories(request):

    all_categories=Category.objects.all() #select all categories(shoes and shirts

    return {'all_categories': all_categories}




