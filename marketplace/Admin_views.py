from django.contrib import messages
from django.shortcuts import render, redirect

from marketplace.forms import PostProducts
from marketplace.models import AddProduct


def admin_dashboard(request):
    return render(request,'Admin/admin.html')

def post_product(request):
    if request.method == 'POST':
        product_forms = PostProducts(request.POST)
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


