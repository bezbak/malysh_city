from django.shortcuts import render, redirect
from apps.users.models import Order
from apps.service.models import Settings
from apps.products.models import Product
# Create your views here.

def buy_product(request, id):
    setting = Settings.objects.latest('id')
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        adres = request.POST.get('adres')
        city = request.POST.get('city')
        phone_number = request.POST.get('phone_number')
        price = request.POST.get('price')
        order = Order.objects.create(first_name = first_name, last_name = last_name, adres = adres,city = city, phone_number = phone_number, price = price, product = product)
        order.save()
        return redirect('product_detail', product.id)
    context = {
        'setting': setting,
        'product': product,
    }
    return render(request, 'main/checkout.html', context)