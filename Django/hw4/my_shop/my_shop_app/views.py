from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(
        request,
        "my_shop_app/catalog.html",
        {"products": products, "categories": categories},
    )


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    context = {"product": product, "categories": categories}
    return render(request, "my_shop_app/product_detail.html", context)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    categories = Category.objects.all()
    context = {"category": category, "products": products, "categories": categories}
    return render(request, "my_shop_app/category_detail.html", context)
