from django.shortcuts import render

from . models import Category, Product

from django.shortcuts import get_object_or_404

# Create your views here.

def store (request):
    all_products = Product.objects.all() #getting hold of all the products

    context = {'all_products':all_products}

    return render(request,'store/store.html', context)

def categories(request):

    all_categories=Category.objects.all() #select all categories(shoes and shirts

    return {'all_categories': all_categories}

def product_info(request,slug):

    product = get_object_or_404(Product,slug=slug) #getting hold of a specific product from a database,
                                                    #if it doesn't exist return an error, match the product with
    context = {'product':product}                   #a slug ID, that is equal to a slug ID we are looking for

    return render(request,'store/product-info.html',context)



