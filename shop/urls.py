from django.urls import path

from . import views

app_name = 'shop'

urlpatterns = [
    # path('', views.homepage, name='homepage'),
    path('', views.list_product_view, name='homepage'),
    path('product/<slug:slug>/', views.product_detail, name='product')
]
