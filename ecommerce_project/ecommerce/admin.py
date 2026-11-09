from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Store, Product, Order, OrderItem, Review


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('User Role', {'fields': ('role',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('User Role', {'fields': ('role',)}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
# Register your models here.
