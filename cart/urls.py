from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>', views.cart_add, name='add'),
    path('remove/<int:product_id>', views.cart_remove, name='remove'),
    path('checkout/', views.checkout_page, name='checkout'),
    path('pdf/views/<int:order_id>/', views.cart_pdf_view, name='pdf'),
    path('pdf/<int:order_id>/', views.generate_order_pdf, name='generate_pdf'),
    path('', views.cartpage, name='cartpage'),
]
