from django.contrib import admin
from .models import HomeModel, AboutModel, MenuModel, contacModel, OrderModel


# Register your models here.

class HomeModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class MenuModelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class contacModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
    search_fields = ['name']
    list_filter = ['name']


class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'number']
    search_fields = ['name']
    list_filter = ['name']


admin.site.register(HomeModel, HomeModelAdmin)
admin.site.register(MenuModel, MenuModelAdmin)
admin.site.register(contacModel, contacModelAdmin)
admin.site.register(AboutModel)
admin.site.register(OrderModel, OrderModelAdmin)
