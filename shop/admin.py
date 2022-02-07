
from django.contrib import admin
from .models import Order, Product
# Register your models here.
admin.site.site_header = "Your Business Site"
admin.site.site_title = "Online Shopping"
admin.site.index_title = "Manage Your Online Business"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    
    change_category_to_default.short_description = ('Default Category')
    actions = ('change_category_to_default',)
    list_display = ('title','price','discount_price','category','description')
    search_fields = ('title','category','description','discount_price')
    # fields = ('title','price','discount_price') #to hide some fields
    list_editable = ('price','discount_price','description','category',)

admin.site.register(Product,ProductAdmin) 
admin.site.register(Order)