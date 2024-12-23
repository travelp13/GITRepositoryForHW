from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseNotAllowed
from .models import Product
from proj.settings import BOT, ADMIN_CHAT_ID
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def main(request: HttpRequest) -> HttpResponse:
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'main/index.html', context)
@csrf_exempt
def send_order(request: HttpRequest):
    if request.method == 'POST':
        product = Product.objects.get(id = request.POST.get("id"))
        BOT.send_message(ADMIN_CHAT_ID, f"New order: {product.name}")
        return HttpResponse(200)
    return HttpResponseNotAllowed()