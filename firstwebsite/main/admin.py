from django.contrib import admin
from main.models import Category,Product,Discount

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Discount)
