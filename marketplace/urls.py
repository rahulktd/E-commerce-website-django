from django.urls import path

from marketplace import views, Admin_views, Buyer_views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login_view',views.login_view,name='login_view'),
    path('logout_view',views.logout_view,name='logout_view'),


    path('admin_dashboard',Admin_views.admin_dashboard,name='admin_dashboard'),
    path('post_product',Admin_views.post_product,name='post_product'),
    path('view_posted',Admin_views.view_posted,name='view_posted'),


    # path('view_products_from_api',Admin_views.view_products_from_api,name='view_products_from_api'),

    path('delete_product/<int:id>/',Admin_views.delete_product,name='delete_product'),
    path('update_product/<int:id>/',Admin_views.update_product,name='update_product'),
    path('admin_cart_view',Admin_views.admin_cart_view,name='admin_cart_view'),
    path('reg_user',Admin_views.reg_user,name='reg_user'),


    path('buyer_dashboard',Buyer_views.buyer_dashboard,name='buyer_dashboard'),
    path('account_buyer',Buyer_views.account_buyer,name='account_buyer'),
    path('account_update_buyer',Buyer_views.account_update_buyer,name='account_update_buyer'),
    path('view_products_to_buy',Buyer_views.view_products_to_buy,name='view_products_to_buy'),
    path('electronics_products',Buyer_views.electronics_products,name='electronics_products'),
    path('fashion_products',Buyer_views.fashion_products,name='fashion_products'),
    path('grocery_products',Buyer_views.grocery_products,name='grocery_products'),
    path('product_view/<int:id>/',Buyer_views.product_view,name='product_view'),
    path('add_to_cart/<int:id>/',Buyer_views.add_to_cart,name='add_to_cart'),
    path('cart_view',Buyer_views.cart_view,name='cart_view'),

    path('like_product/<int:id>/',Buyer_views.like_product,name='like_product'),
    path('unlike_product/<int:id>/',Buyer_views.unlike_product,name='unlike_product'),


]