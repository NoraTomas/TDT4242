import datetime
from django.db import models


CART_ID = 'CART-ID'

class Cart:

    #Init the cart by request:
    def __init__(self, request):
        #get cart id from the request-framework
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)

        else:
            cart = self.new(request)
        self.cart = cart

    def new(self, request):
        #Create a new Cart
        cart = models.Cart(cart = models.Cart())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def update(self):
        #update information about cart?
        return

    def add(self):
        #Add item to cart?
        return

    def delete(self):
        #delete item from cart?
        return

    def count(self):
        #return amount of items in cart
        amount = 0
        for item in self.cart.item_set.all():
            amount = amount + 1
        return amount

    def total_cost(self):
        cost=0
        for item in self.cart.item_set.all():
            cost = cost + item.price
        return cost