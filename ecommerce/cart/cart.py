#session handling class

class Cart():
    def __init__(self,request): #accessing the attributes

        self.session = request.session  #creating new session for new user, returning one utilize existing session
        cart=self.session.get('session_key') #for existing user

    # new key for new user

        if 'session_key' not in request.session:

            cart=self.session['session_key'] = {}

    # new user no products in cart
        self.cart=cart

