from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *
# admin.site.register(Registration)
admin.site.register(UserProfile)
admin.site.register(Item)
