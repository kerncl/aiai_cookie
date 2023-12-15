import weasyprint
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from shop.forms import CartAddProductForm
from .cart import Cart
from .forms import CartForm
from .models import OrderModel, OrderItem


# Create your views here.
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(str(product_id), int(cd['quantity']))
    return redirect('cart:cartpage')
    # return redirect('shop:homepage')
    # return render(request, 'base.html', context={})


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    cart.remove(str(product_id))
    return redirect('cart:cartpage')


@login_required(login_url=reverse_lazy('account:login'))
def cartpage(request):
    cart = Cart(request)
    return render(request, 'cart/cart.html', context={'cart':cart})


@require_POST
def checkout_page(request):
    # 1. get total order
    # 2. get pickup date
    # 3. saved into db
    # 4. generate pdf
    # 5. clear existing cart items
    # 6. download pdf
    # 7. redirect to whatsapp
    cart = Cart(request)
    form = CartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        order = OrderModel(start=cd['start'],
                           end=cd['end'],
                           total_price=cart.total_price)
        order.save()
        for item in cart:
            OrderItem.objects.create(product=item['name'],
                                     quantity=item['quantity'],
                                     price=item['price'],
                                     total_price=item['total_price'],
                                     order=order)
        cart.clear()
        return redirect('shop:homepage')

    return redirect('cart:cartpage')


def generate_order_pdf(request, order_id):
    order = OrderModel.objects.get(order_id=order_id)
    html = render_to_string('cart/order_pdf.html',
                            {'order': order},
                            request)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f"filename=order_{order_id}.pdf"
    weasyprint.HTML(string=html,
                    base_url=request.build_absolute_uri()).write_pdf(response,
                                           stylesheets=[
                                               weasyprint.CSS(
                                                   settings.STATIC_ROOT / 'css/pdf.css'
                                               )
                                           ])

    return response


@login_required(login_url=reverse_lazy('account:login'))
def cart_pdf_view(request, order_id):
    order = OrderModel.objects.get(order_id=order_id)
    return render(request, 'cart/order_pdf.html', {'order':order})
