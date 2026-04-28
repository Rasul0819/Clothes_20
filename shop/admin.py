from django.contrib import admin
from .models import Colors,Clothes,Size,Brand
# Register your models here.

admin.site.register(Colors)

admin.site.register(Brand)
admin.site.register(Size)

class ClothesAdmin(admin.ModelAdmin):
    list_display=['image1','title','brand','description']
    list_display_links=['brand','title']
    list_editable=['description']
    list_filter=['created_date','brand']
    search_fields=['title']



admin.site.register(Clothes,admin_class=ClothesAdmin)