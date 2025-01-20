from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "first_name",
        "last_name",
        "email",
        "city",
        "paid",
        "created",
        "updated",
    ]
    list_filter = ["paid", "created", "updated"]
    search_fields = ["first_name", "last_name", "email"]
    inlines = [OrderItemInline]

    def mark_as_paid(self, request, queryset):
        queryset.update(paid=True)

    mark_as_paid.short_description = "Відзначити вибрані замовлення як оплачені"

    actions = [mark_as_paid]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "product", "price", "quantity"]
    list_filter = ["order"]
    search_fields = ["product__name"]
