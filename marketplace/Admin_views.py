import requests
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from marketplace.forms import PostProducts
from marketplace.models import AddProduct


@login_required(login_url='login_view')
def admin_dashboard(request):
    return render(request,'Admin/admin.html')

@login_required(login_url='login_view')
def post_product(request):
    if request.method == 'POST':
        product_forms = PostProducts(request.POST, request.FILES)
        if product_forms.is_valid():
            add = product_forms.save(commit=False)
            add.save()
            messages.success(request,'Product added successfully')
            return redirect('view_posted')
    else:
        product_form = PostProducts()
    return render(request, 'Admin/product_post_admin.html',{'product_form':product_form})

@login_required(login_url='login_view')
def view_posted(request):
    posted = AddProduct.objects.all()
    return render(request, 'Admin/posted_products.html',{'posted':posted})

@login_required(login_url='login_view')
def delete_product(request,id):
    product = AddProduct.objects.get(id=id)
    product.delete()
    return redirect('view_posted')

@login_required(login_url='login_view')
def update_product(request,id):
    product = AddProduct.objects.get(id=id)
    if request.method == 'Post':
        form = PostProducts(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_posted')
    else:
        form = PostProducts(instance=product)
    return render(request, 'Admin/update_product.html',{'form':form})

# def view_products_from_api(request):
#     response = requests.get('https://fakestoreapi.com/products')
#     products = response.json()
#     return render(request, 'Admin/products_from_api.html', {'products': products})


