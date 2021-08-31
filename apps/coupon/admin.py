from django.contrib import admin

from .models import Coupon

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'value', 'num_available', 'num_used')
    search_fields = ('code', 'value')