from django.contrib import admin

# Register your models here.
from .models import Label, Content, SiteConfig


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ("id", "name")



@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ("id", "summary")





@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = ("id", "background", "total_query", "total_query_success")
    list_editable = ("background", )



