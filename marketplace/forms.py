from django.contrib.auth.forms import UserCreationForm
from django import forms


from marketplace.models import AccReg, AddProduct


class BuyerForm(UserCreationForm):
    class Meta:
        model = AccReg
        fields = ("name","email","mobile","address","username","password1","password2",)

class PostProducts(forms.ModelForm):
    class Meta:
        model =AddProduct
        fields = ("product_name","description","price","image","category","brand","created_date","last_update")



