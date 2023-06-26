import django_filters
from django import forms
from django.db.models import Q
from marketplace.models import AddProduct


class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='search_filter', label='', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 150px; text-align: center;margin: 0 auto;'}))

    class Meta:
        model = AddProduct
        fields = ['search']

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            Q(product_name__icontains=value) |
            Q(brand__icontains=value) |
            Q(category__icontains=value) |
            Q(description__icontains=value)
        )