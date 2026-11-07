from django.shortcuts import render

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, "product.html",)


def recent_products(request):
    return render(request, "")


def product_detail(request):
    return render(request, ".html")
    