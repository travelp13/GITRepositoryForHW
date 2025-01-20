from contextlib import nullcontext
from django.db import models


class ExchangeRate(models.Model):
    currency = models.CharField(max_length=10, unique=True)
    rate_buy = models.DecimalField(max_digits=10, decimal_places=4)
    rate_sell = models.DecimalField(max_digits=10, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.currency}: Buy {self.rate_buy}, Sell {self.rate_sell}"


class Sale(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name="Назва акції")
    slug = models.SlugField(
        max_length=255, unique=True, verbose_name="Slug", blank=True
    )
    description = models.TextField(
        verbose_name="Опис акції",
        null=True,
        blank=True,
        default=None,
    )
    description_html = models.TextField(verbose_name="Опис акції  у HTML")
    image = models.ImageField(
        upload_to="sales/", verbose_name="Зображення", blank=True, null=True
    )
    start_date = models.DateTimeField(verbose_name="Дата початку акції")
    end_date = models.DateTimeField(verbose_name="Дата закінчення акції")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "sale"
        ordering = ["name"]
        verbose_name = "Акція"
        verbose_name_plural = "Акції"


class CarouselSlide(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Заголовок", blank=True, null=True
    )
    image = models.ImageField(upload_to="carousel/", verbose_name="Зображення")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    active = models.BooleanField(default=True, verbose_name="Активний")

    class Meta:
        ordering = ["order"]
        verbose_name = "Слайд"
        verbose_name_plural = "Слайди"

    def __str__(self):
        return self.title or f"Слайд {self.id}"
