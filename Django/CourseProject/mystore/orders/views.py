from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user  # Привязываем заказ к пользователю
            order.save()
            for item in cart:
                # Добавляем товары из корзины в заказ
                order.items.create(
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()  # Очищаем корзину после оформления заказа
            return render(request, "orders/created.html", {"order": order})
    else:
        # Если пользователь авторизован, заполняем форму его данными
        initial_data = {
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        }
        form = OrderCreateForm(initial=initial_data)
    return render(request, "orders/create.html", {"cart": cart, "form": form})
