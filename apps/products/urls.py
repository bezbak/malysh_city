from django.urls import path
from apps.products.views import index, all_products, for_adults,for_kids, search,product_detail

urlpatterns = [
    path('', index, name='index'),
    path('all_products/', all_products, name='all_products'),
    path('product_detail/<int:id>/', product_detail, name='product_detail'),
    path('for_adults/', for_adults, name='for_adults'),
    path('for_kids/', for_kids, name='for_kids'),
    path('search/', search, name='search'),
]
