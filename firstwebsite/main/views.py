from django.shortcuts import render
from main.models import Category,Product
from django.core.paginator import Paginator

# Create your views here.
def base(response):
    return render(response,"main/index.html",{})

def product_detail(response,name):
    product=Product.objects.get(name=name)
    categories= Category.objects.all()
    return render(response,"main/product-details.html",{'categories':categories,'product':product})

def shop(response):
    products=Product.objects.all()
    paginator=Paginator(products,12)
    page_number = response.GET.get('page')
    page_obj = paginator.get_page(page_number)  
    categories= Category.objects.all()
    return render(response,"main/shop.html",{'categories':categories,'products':page_obj})
