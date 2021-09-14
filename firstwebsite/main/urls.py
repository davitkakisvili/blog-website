from django.urls import path
from . import views

urlpatterns=[
    path("", views.base,name="index"),
    path("shop",views.shop,name="shop" ),
    path("shop/<str:name>",views.product_detail,name="product-details"),

    ]