from django.contrib import admin
from library.models import BookAuth, Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','is_active','is_rare','is_DrawTool']


@admin.register(BookAuth)
class BookAuthAdmin(admin.ModelAdmin):
    list_display = ['id','name','email']

