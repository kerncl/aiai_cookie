from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404

from shop.models import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1):
        product = get_object_or_404(Product, id=product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.name,
                'quantity': 0,
                'price': str(product.price)
            }
        self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product_id):
        del self.cart[product_id]
        self.save()

    def __iter__(self):
        for id_, product in self.cart.items():
            product_obj = get_object_or_404(Product, id=id_)
            product['total_price'] = product['quantity'] * Decimal(product['price'])
            product['id'] = id_
            product['image'] = product_obj.image.url
            yield product

    @property
    def total_price(self):
        return sum(item['total_price'] for item in self)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]

    @property
    def total_item(self):
        return len(self.cart)

    def __len__(self):
        return sum(item['quantity'] for item in self)

    def save(self):
        self.session.modified = True

    def __str__(self):
        txt = ''
        for t in self:
            txt += f"{t['name']}: {t['quantity']}"
        return txt




