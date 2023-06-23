from django.urls import path

from marketplace import views, Admin_views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('login_view',views.login_view,name='login_view'),


    path('admin_dashboard',Admin_views.admin_dashboard,name='admin_dashboard'),
    path('post_product',Admin_views.post_product,name='post_product'),
    path('view_posted',Admin_views.view_posted,name='view_posted'),
    path('delete_product/<int:id>/',Admin_views.delete_product,name='delete_product'),
    path('update_product/<int:id>/',Admin_views.update_product,name='update_product'),
]