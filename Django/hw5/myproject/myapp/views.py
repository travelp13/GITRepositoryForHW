from django.shortcuts import render, redirect
from .forms import ProductForm, ProductReviewForm
from .models import Product
from django.http import HttpResponse


def main_page(request):
    return HttpResponse(
        """
        <h1>Головна сторінка</h1>
        <a href="/create/">Сторінка create</a><br>
        <a href="/list/">Сторінка list</a><br>
        <a href="/submit-review/">Сторінка submit-review</a><br>
        <a href="/review-success/">Сторінка review-success</a><br>
    """
    )


def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "myapp/product_form.html", {"form": form})


def product_list(request):
    products = Product.objects.all()
    return render(request, "myapp/product_list.html", {"products": products})


def submit_review(request):
    if request.method == "POST":
        form = ProductReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("review_success")
    else:
        form = ProductReviewForm()
    return render(request, "myapp/submit_review.html", {"form": form})


def review_success(request):
    return render(request, "myapp/review_success.html")
