from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from app_iso.models import Category, Blogs
# Create your views here.

def HomePage(request):
    return render(request,"home.html")

def NewsBlog(request):
    categories = Category.objects.all()
    blogs = Blogs.objects.all()
    latest = Blogs.objects.all().order_by('-pk')[:2]

    context = {
        'categories':categories,
        'blogs':blogs,
        'latest':latest
    }
    return render(request,"NewsAndEvent.html",context)

def Register(request):
    if request.method == 'POST':
        data = request.POST.copy()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')

        newuser = User()
        newuser.username = email
        newuser.first_name = first_name
        newuser.last_name = last_name
        newuser.email = email
        newuser.set_password(password)
        newuser.save()
        return redirect('login')

    return render(request, 'register.html')

def Contact(request):
    return render(request,"contact.html")