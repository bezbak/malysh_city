from django.shortcuts import render
from apps.service.models import Settings
from apps.products.models import Product
from django.db.models import Q
# Create your views here.
def index(request):
    setting = Settings.objects.latest('id')
    slider = Product.objects.all().filter(sale = True)[:4]
    products = Product.objects.all()[:16]
    context = {
        'setting': setting,
        'slider':slider,
        'products':products
    }
    return render(request, 'main/index.html',context)

def product_detail(request,id):
    setting = Settings.objects.latest('id')
    product = Product.objects.get(id=id)
    context = {
        'setting': setting,
        'product': product,
    }
    return render(request, 'main/product_detail.html',context)
    

def all_products(request):
    setting = Settings.objects.latest('id')
    products = Product.objects.all()
    context = {
        'setting': setting,
        'products':products
    }
    return render(request, 'main/all_products.html',context)
    
def for_kids(request):
    setting = Settings.objects.latest('id')
    products = Product.objects.all().filter(category__name='Для детей')
    context = {
        'setting': setting,
        'products':products
    }
    return render(request, 'main/for_kids.html',context)

def for_adults(request):
    setting = Settings.objects.latest('id')
    products = Product.objects.all().filter(category__name='Для подростков')
    context = {
        'setting': setting,
        'products':products
    }
    return render(request, 'main/for_adults.html',context)

def search(request):
    setting = Settings.objects.latest('id')
    products = Product.objects.all()
    search_key = request.GET.get('key')
    if search_key:
        products = Product.objects.filter(Q(title__icontains = search_key))
    context = {
        'setting': setting,
        'products':products
    }
    return render(request,'main/search.html', context)