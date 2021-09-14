from django.urls import path,include

from . import views

urlpatterns=[
    path("", views.blog,name="blog"),
    path("register/", views.register,name="register"),
    path('',include('django.contrib.auth.urls')),
    path("<str:name>/", views.blog_single,name="blog"),
   
    ]