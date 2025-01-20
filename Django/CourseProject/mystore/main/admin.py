from django.contrib import admin
from .models import Sale, CarouselSlide


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("name", "start_date", "end_date")
    list_filter = ("start_date", "end_date")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "active")
    list_editable = ("order", "active")
    ordering = ("order",)
