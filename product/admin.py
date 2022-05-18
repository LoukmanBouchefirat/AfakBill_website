from django.contrib import admin
from .models import Category, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'visits','condition',  'n_price', 'r_price', 'in_stock', 'created', 'updated', 'is_newproduct']
    list_filter = ['in_stock']
    list_editable = ['n_price', 'r_price', 'in_stock','is_newproduct']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register({ProductImage})


