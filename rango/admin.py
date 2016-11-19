from django.contrib import admin
from rango.models import Category, Page, UserProfile

class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name', 'views', 'likes', 'popular')
  prepopulated_fields = { 'slug': ('name', ) }

# class to customize page view in /admin
class PageAdmin(admin.ModelAdmin):
  list_display = ('title', 'category', 'views')
  list_filter = ('category',)
  fieldsets = [
    ('Category', {'fields': ['category']}),
    ('Page information', {'fields': ['title', 'slug', 'views'], 'classes': ['collapse']}),
  ]

# register models to make them accessible via the /admin interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)

