class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if 'cart' not in self.session or not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    def add_product(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] += int(quantity)
        else:
            self.cart[product_id] = {'quantity': int(quantity)}

        self.save()

    def remove_product(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session['cart'] = self.cart
        self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True
