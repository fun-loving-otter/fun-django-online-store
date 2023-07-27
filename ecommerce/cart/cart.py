#session handling class

class Cart():
    def __init__(self,request): #accessing the attributes

        self.session = request.session  #creating new session for new user, returning one utilize existing session
        cart=self.session.get('session_key') #for existing user

        # new key for new user
        if 'session_key' not in request.session:

            cart=self.session['session_key'] = {}

        self.cart=cart         # new user no products in cart



    def add(self,product,product_qty):                   #passing add function into an add class

        product_id = str(product.id)                     #str so only the quantity can get modified

        if product_id in self.cart:                       #if product is in the cart

            self.cart[product_id]['qty'] = product_qty     #modifying the quantity if necessary

        else:                                               #if the product not in the cart, taking the price and qty

            self.cart[product_id] = {'price':str (product.price),'qty':product_qty}

        self.session.modified = True                        #the session has been modified

    def __len__(self):                                                  #total length of products in a session

        return sum(item['qty'] for item in self.cart.values())         #total number of items in a shopping cart