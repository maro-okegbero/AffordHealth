from django.contrib import admin
from app.models import *
# Register your models here.

admin.site.site_header = 'Afford Health Dashboard'

admin.site.register(BlogPost)
admin.site.register(Cause)
admin.site.register(CustomUser)
admin.site.register(Category)




