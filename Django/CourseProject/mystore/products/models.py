from ast import Return
from locale import currency
from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from main.models import ExchangeRate


class Currency(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name="Валюта")
    char_code = models.CharField(max_length=3, verbose_name="Код Валюти")
    int_code = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(999)],
        verbose_name="Цифровий код валюти",
    )

    class Meta:
        db_table = "currency"
        ordering = ["name"]
        verbose_name = "Валюта"
        verbose_name_plural = "Валюти"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Назва категорії")
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name="Slug", blank=True
    )
    description = models.TextField(blank=True, verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")

    class Meta:
        db_table = "category"
        ordering = ["name"]
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва продукту")
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name="Slug", blank=True
    )
    description = models.TextField(blank=True, verbose_name="Короткий опис")
    long_description = models.TextField(
        verbose_name="Детальний опис", null=True, blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name="Категорія",
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name="Валюта",
    )
    sku = models.CharField(max_length=50, verbose_name="Код продукту", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата оновлення")
    is_active = models.BooleanField(default=True, verbose_name="Ознака активності")
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True,
        verbose_name="Зображення продукту",
    )
    discount = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, verbose_name="Знижка"
    )

    class Meta:
        db_table = "product"
        ordering = ["name"]
        verbose_name = "Продукт"
        verbose_name_plural = "Продукти"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    @staticmethod
    def round_to_next_99(number):
        # Округляем до ближайшего числа, заканчивающегося на 99
        return number + (99 - number % 100)

    def get_price_in_uah(self):
        product_price = self.price
        if self.currency.char_code == "USD":
            try:
                exchange_rate = ExchangeRate.objects.get(currency="USD").rate_sell
            except ExchangeRate.DoesNotExist:
                exchange_rate = 1
            product_price *= exchange_rate

        return self.round_to_next_99(round(product_price, 2))

    def get_price_with_discount(self):
        product_price = self.get_price_in_uah()

        if self.discount > 0:
            product_price = product_price * (1 - (self.discount / 100))

        return self.round_to_next_99(round(product_price, 2))
