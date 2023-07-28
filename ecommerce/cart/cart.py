#session handling class, available on every page via context processor
from decimal import Decimal

from store.models import Product
class Cart():
    def __init__(self,request):                                                              #accessing the attributes

        self.session = request.session                                                       #creating new session for new user, returning one utilize existing session
        cart=self.session.get('session_key')                                                 #for existing user

        # new key for new user
        if 'session_key' not in request.session:

            cart=self.session['session_key'] = {}

        self.cart=cart                                                                      # new user no products in cart



    def add(self,product,product_qty):                                                     #passing add function into an add class

        product_id = str(product.id)                                                        #str so only the quantity can get modified

        if product_id in self.cart:                                                          #if product is in the cart

            self.cart[product_id]['qty'] = product_qty                                       #modifying the quantity if necessary

        else:                                                                                #if the product not in the cart, taking the price and qty

            self.cart[product_id] = {'price':str (product.price),'qty':product_qty}

        self.session.modified = True                                                         #the session has been modified

    def delete(self,product):

        product_id=str(product)

        if product_id in self.cart:

            del self.cart[product_id]

        self.session.modified = True


    def update(self,product, qty):

        product_id = str(product)
        product_quantity = qty

        if product_id in self.cart:

            self.cart[product_id]['qty'] = product_quantity

        self.session.modified = True


    def __len__(self):                                                                                #total length of products in a session

        return sum(item['qty'] for item in self.cart.values())                                        #total number of items in a shopping cart





    def __iter__(self):

        all_product_ids = self.cart.keys()

        products = Product.objects.filter(id__in=all_product_ids)                            #checking if products in cart matche the database

        cart = self.cart.copy()

        for product in products:

            cart[str(product.id)]['product']=product

        for item in cart.values():                                                            #for loop for price

            item['price']=Decimal(item['price'])

            item['total'] = item['price'] *item['qty']                                         #multiply the price by quantity

            yield item


    def get_total(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
