from django.contrib import admin
from .models import Profile, Experience
 
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'nickname', 'email']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ['title', 'company', 'start_date', 'is_current']
    list_filter   = ['is_current']
    ordering      = ['-start_date']