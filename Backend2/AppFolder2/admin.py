from django.contrib import admin

# Register your models here.
from .models import User2
# Register your models here.
admin.site.site_title = 'log-admin'
admin.site.site_header= 'LOG-IN'
#admin.site.site_index = 'Welcome back'


class UserAdmin2(admin.ModelAdmin):
    list_display = ('name','email')

     
admin.site.register(User2,UserAdmin2)