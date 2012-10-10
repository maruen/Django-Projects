from salesman.register.models import Product
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin


class AdminProduct(ModelAdmin):
   list_display=('name','pictureURL')

admin.site.register(Product,AdminProduct)


