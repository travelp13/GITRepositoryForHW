from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from functools import wraps
from .models import ExchangeRate, Sale, CarouselSlide
from products.models import Product
from django.utils.timezone import now


def index(request):
    exchange_rate = ExchangeRate.objects.filter(currency="USD").first()
    exchange_rate.rate_sell = round(exchange_rate.rate_sell, 2)
    slides = CarouselSlide.objects.filter(active=True)
    products = Product.objects.filter(is_active=True, discount__gt=0)[:19]
    context = {"exchange_rate": exchange_rate, "products": products, "slides": slides}
    return render(request, "main/index.html", context)


def sale_list(request):
    sales = Sale.objects.filter(end_date__gte=now()).order_by("start_date")
    context = {"sales": sales}
    return render(request, "main/sale_list.html", context)


def sale_detail(request, slug):
    sale = get_object_or_404(Sale, slug=slug)
    return render(request, "main/sale_detail.html", {"sale": sale})


def contacts(request):
    return render(request, "main/contacts.html")


def about(request):
    return render(request, "main/about.html")


def delivery(request):
    return render(request, "main/delivery.html")


def offer(request):
    return render(request, "main/offer.html")


def guarantee(request):
    return render(request, "main/guarantee.html")


def privacy_policy(request):
    return render(request, "main/privacy_policy.html")
