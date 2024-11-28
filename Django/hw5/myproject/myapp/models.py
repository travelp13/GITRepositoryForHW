from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва продукту")
    description = models.TextField(verbose_name="Опис продукту")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    stock = models.IntegerField(verbose_name="Кількість на складі")

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    RATING_CHOICES = [
        (1, "1 - дуже погано"),
        (2, "2 - погано"),
        (3, "3 - середньо"),
        (4, "4 - добре"),
        (5, "5 - відмінно"),
    ]
    REVIEW_CHOICES = [
        ("positive", "Позитивний"),
        ("negative", "Негативний"),
    ]

    product_name = models.CharField(max_length=255, verbose_name="Назва продукту")
    user_email = models.EmailField(verbose_name="Пошта користувача")
    description = models.TextField(verbose_name="Опис відгуку")
    rating = models.IntegerField(choices=RATING_CHOICES, verbose_name="Оцінка")
    review_type = models.CharField(
        max_length=10, choices=REVIEW_CHOICES, verbose_name="Тип відгуку"
    )
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефону")
    image = models.ImageField(
        upload_to="reviews/", null=True, blank=True, verbose_name="Зображення"
    )

    def __str__(self):
        return f"Відгук про {self.product_name} від {self.user_email}"
