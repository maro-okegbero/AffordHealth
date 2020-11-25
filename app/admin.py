from django.contrib import admin
from app.models import *

# Register your models here.


admin.site.site_header = 'Afford Health Dashboard'


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "image", "author")
    list_filter = ("author", "category")
    search_fields = ("title", "body")


admin.site.register(Cause)
admin.site.register(CustomUser)
admin.site.register(Category)
