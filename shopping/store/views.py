from django.shortcuts import render

# Create your views here.

def store(request):
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request,'store/cart.html')

def checkout(request):
    context = {}
    return render(request,'store/checkout.html') 