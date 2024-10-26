from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from firstapp.models import wishlist, Product
@login_required(login_url='login')
def index(request):
    wishlistitems = wishlist.objects.filter(user=request.user)
    context = {'wishlistitems':wishlistitems}
    return render(request, 'firstapp/products/wishlist.html', context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if product_check:
                if (wishlist.objects.filter(user=request.user, product_id=prod_id)):
                    return JsonResponse({'status':"Product already on wishlist"})
                else:
                    wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status':"Product added to Wishlist"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')

def deletewishlistitem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if (wishlist.objects.filter(user=request.user, product_id=prod_id)):
                wishlistitem = wishlist.objects.get(product_id=prod_id)
                wishlistitem.delete()
                return JsonResponse({'status':"Product removed from wishlist"})
            else:
                return JsonResponse({'status':"Product not founded in Wishlist"})
        else:
            return JsonResponse({'status':"Login to continue"})
    return redirect('/')