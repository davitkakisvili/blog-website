from django.contrib.auth import get_user
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.paginator import Paginator
from blog.models import Post,Reply,Tag,User
from blog.forms import RegisterForm,CommentForm

# Create your views here.
def blog(response):
    posts=Post.objects.all()
    paginator=Paginator(posts,5)
    page_number = response.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(response,"main/blog.html",{"posts":page_obj,})


def blog_single(response,name):
    if response.method == "GET":
        post=Post.objects.get(title=name)
        form=CommentForm()
        return render(response,"main/blog-single.html",{"post":post,'commentForm':form})
    if response.method == "POST":
        post=Post.objects.get(title=name)
        form=CommentForm(response.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            if response.user.is_authenticated:
                instance.writer=get_user(response)
            else:
                instance.writer=User.objects.get(username="Anonymous")     
            instance.post=post 
            instance.save()
            return redirect('/blog')
        else:
            return redirect('/')   


            
        

def register(response):
    if response.method == "GET":
        form  = RegisterForm()
        context = {'form': form}
        return render(response, 'blog/register.html', context)
    if response.method == "POST":
        form=RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(response,'Account Created For'+user)
            return redirect('/blog')
        else:
            print('Form is not valid')
            messages.error(response, 'Error Processing Your Request')
            context = {'form': form}
            return render(response, 'blog/register.html', context)
    return render(response, 'blog/register.html', {})        



       
