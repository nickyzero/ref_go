from django.contrib import admin
from .models import Refrigerator, Categories ,Location, Product, Inventory, Cleancheck, Memo, Shopping_list, Setting_user

class ShoppinglistAdmin(admin.ModelAdmin):
    list_display = ('user','product','count','price')
    list_filter = ('user',)

admin.site.register(Categories)
admin.site.register(Refrigerator)
admin.site.register(Location)
admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Cleancheck)
admin.site.register(Memo)
admin.site.register(Shopping_list,ShoppinglistAdmin)
admin.site.register(Setting_user)
