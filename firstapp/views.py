from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    slide = slider.objects.all()
    trending_products = Product.objects.filter(trending=1)
    context = {'trending_products':trending_products, 'slide':slide}
    return render(request, 'firstapp/index.html', context)
    

def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category' :category}
    return render(request, "firstapp/collections.html", context,)

def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug, status=0)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, "firstapp/products/index.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('collections')

def productview(request, cate_slug, prod_slug):
    if (Category.objects.filter(slug=cate_slug, status=0)):
        if (Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products':products}
        else:
            messages(request, "No such Products found")
            return redirect('collections')
    else:
        messages(request, "No such category found")
        return redirect('collections')
    return render(request, "firstapp/products/view.html", context)

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered")
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                messages.success(request, "Registration successful")
                user = authenticate(username=username, password=password)
                #if user is not None:
                    #login(request, user)
                    #return redirect('signup')  # Redirect to the home page or another appropriate page after successful registration.
    # If the request method is not POST or if there are errors, display the signup form.
    return render(request, "firstapp/form/signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Login Successful')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, "firstapp/form/login.html")

def logout_user(request):
    auth.logout(request)
    messages.info(request, 'Logout Successful')
    return redirect('home')
    #return render(request, 'firstapp/index.html')

