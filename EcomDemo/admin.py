from django.contrib import admin
from EcomDemo.models import User, Product

# admin.site.register(User)
# admin.site.register(Product)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'email', 'name']
    list_display = ['id','username', 'name']
    search_fields = ['name','id']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'description','stock']
    list_display = ['id', 'name', 'price', 'stock']
    search_fields = ['name']