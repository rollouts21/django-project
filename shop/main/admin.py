from django.contrib import admin

from .models import Product, Service, Category, About


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "price",
        "available",
        "created",
        "updated",
        "amount",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available", "amount"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "price", "available"]
    list_filter = ["available"]
    prepopulated_fields = {"slug": ("name",)}
