from django.contrib import admin

from marketplace.models import AccReg, AddProduct,Cart,LikeProduct

# Register your models here.
admin.site.register(AccReg),
admin.site.register(AddProduct),
admin.site.register(Cart),
admin.site.register(LikeProduct),
