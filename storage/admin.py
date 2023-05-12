from django.contrib import admin

from storage.models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "upload", "is_deleted")