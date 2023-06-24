from django.shortcuts import render, redirect

from marketplace.forms import BuyerProfileForm
from marketplace.models import AddProduct


def buyer_dashboard(request):
    return render(request,'Buyer/buyer_dashboard.html')

def view_products_to_buy(request):
    data = AddProduct.objects.all()
    return render(request, 'Buyer/view_products_to_buy.html',{'data':data})

def product_view(request,id):
    product = AddProduct.objects.get(id=id)
    return render(request, 'Buyer/product_view.html',{'product':product})

def account_buyer(request):
    user = request.user
    return render(request,'Buyer/account_buyer.html',{'user':user})

def account_update_buyer(request):
    user =request.user
    if request.method == 'POST':
        profile = BuyerProfileForm(request.POST, instance=user)
        if profile.is_valid():
            profile.save()
            return redirect('account_buyer')
    else:
        profile = BuyerProfileForm(instance=user)
    return render(request, 'Buyer/buyer_profile_update.html',{'profile':profile})

def electronics_products(request):
    electronics = AddProduct.objects.filter(category='ec')
    return render(request, 'Buyer/electronics_products.html', {'electronics': electronics})

def fashion_products(request):
    fashion = AddProduct.objects.filter(category='fs')
    return render(request, 'Buyer/fashion_products.html', {'fashion': fashion})

def grocery_products(request):
    grocery = AddProduct.objects.filter(category='gc')
    return render(request, 'Buyer/grocery_products.html', {'grocery': grocery})



