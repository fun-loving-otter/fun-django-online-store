from django.shortcuts import render

from.cart import Cart #importing cart class from the Cart

from store.models import Product
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

# Create your views here.


def cart_summary(request):

    cart = Cart(request)

    return render(request,'cart/cart-summary.html',{'cart':cart})


def cart_add(request):                           #grabbing AJAX functionality from product-info

    cart=Cart(request)                            #using session data

    if request.POST.get('action') =='post':       #verifying AJAX request, if correct accessing it

        product_id= int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        #performing a query on a Product class object that is equal to AJAX request

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)      #getting a particular product along with its quantity


        cart_quantity = cart.__len__()                               #total quantity from session data


        response = JsonResponse({'qty':cart_quantity})

        return response

def cart_delete(request):

    pass


def cart_update(request):

    pass