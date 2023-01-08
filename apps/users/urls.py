from django.urls import path
from apps.users.views import buy_product

urlpatterns = [
    path('buy/<int:id>/', buy_product, name='buy_product')
]
