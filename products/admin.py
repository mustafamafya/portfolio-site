from django.contrib import admin
from .models import Product, pro_gallery,product_review # ✅ import the model correctly
import admin_thumbnails

@admin_thumbnails.thumbnail('image')
class ProductGalleryInline(admin.TabularInline):  # ✅ proper naming
    model = pro_gallery
    extra = 1
    verbose_name_plural = "Product Gallery"


    
   

class ProductAdmin(admin.ModelAdmin):

    inlines = [ProductGalleryInline]  # ✅ matches the class name


# our registred models
admin.site.register(Product, ProductAdmin)
admin.site.register(pro_gallery)
admin.site.register(product_review)
