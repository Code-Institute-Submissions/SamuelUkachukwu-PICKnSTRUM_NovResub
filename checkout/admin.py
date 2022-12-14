from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_cart',
        'stripe_pid'
        )

    fields = (
        'user_profile',
        'full_name',
        'order_number',
        'email',
        'phone_number',
        'date',
        'street_address1',
        'street_address2',
        'town_or_city',
        'postcode',
        'county',
        'country',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_cart',
        'stripe_pid'
        )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'order_total',
        'delivery_cost',
        'grand_total',
        )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
