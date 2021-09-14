from django.contrib import admin
from blog.models import Post,Comment,Reply,Tag,Profile
# Register your models here.


# Register your models here.
admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Profile)
