from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Category)
class category_mod_reg(admin.ModelAdmin):
    list_display = ["id","name"]


@admin.register(Brand)
class brand_mod_reg(admin.ModelAdmin):
    list_display = ["id","brand_name","category"]


@admin.register(ProductModel)
class product_mod_reg(admin.ModelAdmin):
    list_display = [
        "id",
        "brand",
        "category",
        "image",
        "item_title",
        "item_desc",
        "price",
        "item_discount_price",
        "off",
        "Trending_product",
        # "Slider_product",
        "Promotion_product",
    ]

@admin.register(Slider)
class slider(admin.ModelAdmin):
    list_display = ["id","product","background_img"]

@admin.register(ProductDescription)
class ProductDescModl(admin.ModelAdmin):
    list_display = ["name", "desc", "image"]

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ["name", "title", "review", "rating","product"]
