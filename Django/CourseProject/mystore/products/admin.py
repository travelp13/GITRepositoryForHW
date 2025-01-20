from django.contrib import admin
from .models import Currency, Product, Category
from django.utils.safestring import mark_safe


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "image_show",
        "price",
        "currency",
        "discount",
        "is_active",
        "created_at",
    )
    list_filter = (
        "is_active",
        "category",
        "price",
        "currency",
        "discount",
        "created_at",
    )
    search_fields = ("name", "description", "is_active")
    ordering = (
        "name",
        "is_active",
        "category",
        "price",
        "currency",
        "discount",
        "created_at",
    )
    prepopulated_fields = {"slug": ("name",)}

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Зображення"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Currency)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
