from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from marketplace.filters import ProductFilter
from marketplace.forms import BuyerProfileForm
from marketplace.models import AddProduct, Cart


@login_required(login_url='login_view')
def buyer_dashboard(request):
    data = AddProduct.objects.all()
    data_filter = ProductFilter(request.GET, queryset=data)
    return render(request,'Buyer/buyer_dashboard.html',{'data_filter':data_filter})

@login_required(login_url='login_view')
def view_products_to_buy(request):
    data = AddProduct.objects.all()
    data_filter = ProductFilter(request.GET, queryset=data)
    data = data_filter.qs
    return render(request, 'Buyer/view_products_to_buy.html',{'data':data,'data_filter':data_filter})


@login_required(login_url='login_view')
def product_view(request,id):
    product = AddProduct.objects.get(id=id)
    return render(request, 'Buyer/product_view.html',{'product':product})

@login_required(login_url='login_view')
def account_buyer(request):
    user = request.user
    return render(request,'Buyer/account_buyer.html',{'user':user})

@login_required(login_url='login_view')
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

@login_required(login_url='login_view')
def electronics_products(request):
    electronics = AddProduct.objects.filter(category='ec')
    return render(request, 'Buyer/electronics_products.html', {'electronics': electronics})

@login_required(login_url='login_view')
def fashion_products(request):
    fashion = AddProduct.objects.filter(category='fs')
    return render(request, 'Buyer/fashion_products.html', {'fashion': fashion})

@login_required(login_url='login_view')
def grocery_products(request):
    grocery = AddProduct.objects.filter(category='gc')
    return render(request, 'Buyer/grocery_products.html', {'grocery': grocery})

@login_required(login_url='login_view')
def add_to_cart(request, id):
    product = AddProduct.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    return render(request, 'Buyer/cart.html', {'cart': cart})

@login_required(login_url='login_view')
def cart_view(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.products.all()
    return render(request, 'Buyer/cart_view.html', {'cart': cart, 'products': products})





