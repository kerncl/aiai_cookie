from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import OrderModel, OrderItem

# Register your models here.


def order_pdf(obj):
    url = reverse('cart:generate_pdf', args=[obj.order_id])
    return mark_safe(f"<a href='{url}'>PDF</a>")


order_pdf.description = 'Invoice'


class OrderInline(admin.TabularInline):
    model = OrderItem
    fields = ('product', 'quantity', 'price','total_price')
    readonly_fields = ('product', 'price')
    ordering = ('product',)
    list_filter = ('price', 'quantity', 'total_price')


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','updated', 'start', 'end', 'get_products','total_price', 'delivered', order_pdf)
    inlines = [OrderInline]
    list_editable = ['delivered']
    list_filter = ['delivered', 'created', 'updated']
    readonly_fields = ('total_price',)
    # fields = [order_pdf]

    @admin.display(description='products')
    def get_products(self, obj):
        return [item.product for item in obj.orderitem_set.all()]
