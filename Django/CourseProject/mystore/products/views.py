from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Category
from cart.forms import CartAddProductForm


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "products/product_detail.html", {"product": product})


def catalog(request):
    categories = Category.objects.all()
    selected_category_id = request.GET.get(
        "category"
    )  # Получаем ID категории из GET-запроса

    if selected_category_id:
        selected_category = get_object_or_404(Category, id=selected_category_id)
        products = Product.objects.filter(
            category=selected_category
        )  # Фильтруем продукты
    else:
        selected_category = None
        products = (
            Product.objects.all()
        )  # Если категория не выбрана, показываем все продукты

    # Пагинация
    paginator = Paginator(products, 12)  # 6 продуктов на страницу
    page_number = request.GET.get(
        "page"
    )  # Получаем номер текущей страницы из GET-запроса
    page_obj = paginator.get_page(page_number)  # Получаем нужную страницу продуктов

    form = CartAddProductForm()
    return render(
        request,
        "products/catalog.html",
        {
            "categories": categories,
            "products": page_obj,  # Передаем объект пагинации вместо всех продуктов
            "selected_category": selected_category,
            "form": form,
        },
    )
