from django.contrib import admin
from .models import Category,Product



admin.site.register(Category)
admin.site.register(Product)


# from django.contrib import admin
# from .models import Product,Category

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['name', 'category', 'price', 'stock']
#     fields = ('category', 'name', 'slug', 'description',
#               'price', 'stock',
#               'image_url',   # show URL field
#               'image')       # show file upload

# admin.site.register(Product, ProductAdmin)
