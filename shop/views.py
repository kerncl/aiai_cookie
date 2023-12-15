from django.shortcuts import render

from .models import Product
from .forms import CartAddProductForm


# Create your views here.
def homepage(request):
    return render(request, 'base.html')


def list_product_view(request):
    p = Product.objects.filter(available=True)
    return render(request, 'shop/list.html', context={'products': p})


def product_detail(request, slug):
    p = Product.objects.get(slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/detail.html',
                  context={'product':p,
                           'cart_product_form': cart_product_form})
