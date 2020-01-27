from django.contrib import admin
from .models import Photos,AccessLog,Profile
# Register your models here.


@admin.register(Photos)
class PhotoAdmin(admin.ModelAdmin):
	list_display = ('profile',)
	list_filter = ('profile',)
	search_fields = ['profile__name']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('name','designation','gender','age','phone_no','email')
	list_filter = ('name','designation','gender')
	search_fields = ['name','designation','email','phone_no']

@admin.register(AccessLog)
class AccessLogAdmin(admin.ModelAdmin):
	list_display = ('profile','entry_time','exit_time')
	list_filter = ('profile',)
	search_fields = ['profile__name']

