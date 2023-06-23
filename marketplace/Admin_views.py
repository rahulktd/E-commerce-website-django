from django.contrib import messages
from django.shortcuts import render, redirect

from marketplace.forms import PostProducts
from marketplace.models import AddProduct


def admin_dashboard(request):
    return render(request,'Admin/admin.html')

def post_product(request):
    if request.method == 'POST':
        product_forms = PostProducts(request.POST, request.FILES)
        if product_forms.is_valid():
            add = product_forms.save(commit=False)
            add.save()
            messages.success(request,'Product added successfully')
            return redirect('index')
    else:
        product_form = PostProducts()
    return render(request, 'Admin/product_post_admin.html',{'product_form':product_form})

def view_posted(request):
    posted = AddProduct.objects.all()
    return render(request, 'Admin/posted_products.html',{'posted':posted})

def delete_product(request,id):
    product = AddProduct.objects.get(id=id)
    product.delete()
    return redirect('view_posted')

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


