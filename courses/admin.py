from django.contrib import admin
from .models import User,Comment,Video,Course
# Register your models here.

class VideoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Video,VideoAdmin)
admin.site.register(Course,CourseAdmin)
