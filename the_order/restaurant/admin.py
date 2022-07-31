from django.contrib import admin
from .models import Restaurant, Category, Product, Order, ProductOrder

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "restaurant") 

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ("order", "product") 

admin.site.register(Restaurant)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductOrder, ProductOrderAdmin)





