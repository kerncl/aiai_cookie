from django.contrib import admin
from .models import Product


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available', 'created', 'updated']
    list_editable = ['available']
    fields = [('name', 'slug'),'price', 'available', 'description', 'image_tag', 'image']   # EDIT PAGE
    readonly_fields = ['image_tag']
