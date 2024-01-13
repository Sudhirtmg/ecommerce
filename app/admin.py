from django.contrib import admin
from .models import *

# Register your models here.
class Product_Images(admin.TabularInline):
    model=Product_Image
class Additional_Informations(admin.TabularInline):
    model=Additional_Information

class Product_Admin(admin.ModelAdmin):
    inlines=(Product_Images,Additional_Informations)
    
admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Additional_Information)

admin.site.register(Slider)
admin.site.register(Banner)
admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)


