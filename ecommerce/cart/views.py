from django.shortcuts import render

from.cart import Cart #importing cart class from the Cart

from store.models import Product
from django.shortcuts import get_object_or_404

from django.http import JsonResponse

# Create your views here.


def cart_summary(request):

    return render(request,'cart/cart-summary.html')


def cart_add(request):                           #grabbing AJAX functionality from product-info

    cart=Cart(request)                            #using session data

    if request.POST.get('action') =='post':       #verifying AJAX request, if correct accessing it

        product_id= int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))

        #performing a query on a Product class object that is equal to AJAX request

        product = get_object_or_404(Product, id=product_id)

        cart.add(product=product, product_qty=product_quantity)      #getting a particular product along with its quantity

        response = JsonResponse({'The product is called:': product.title, 'and the product quantity is:':product_quantity})

        return response

def cart_delete(request):

    pass


def cart_update(request):

    pass