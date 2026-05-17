from django.contrib import admin
from .models import Dashboard, Banner, GalleryItem, About

# For Configuration of tables
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title', 'add_date')
    search_fields = ('title',)
    
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('banner_title', 'add_date')
    
# Register your models here.
admin.site.register(Dashboard, DashboardAdmin)
admin.site.register(Banner, CategoryAdmin)
admin.site.register(GalleryItem)
admin.site.register(About)