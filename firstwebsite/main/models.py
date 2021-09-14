from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.name
 
class Discount(models.Model):
    name=models.CharField(max_length=200)
    desc=models.TextField()
    discount_percent=models.DecimalField(max_digits=3, decimal_places=2)
    active=models.BooleanField(default=False    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.name



class Product(models.Model):
    name=models.CharField(max_length=200)
    image = models.ImageField(upload_to="photos/%Y/%m/%d",default='photos/default.png')
    desc=models.TextField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    discount=models.ForeignKey(Discount,on_delete=models.CASCADE,blank=True,null=True)
    inventory=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.name

