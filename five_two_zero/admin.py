from django.contrib import admin

# Register your models here.
from .models import Content, LeaveMessage, Key, Question


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    # list_display = ()
    pass

@admin.register(LeaveMessage)
class LeaveMessageAdmin(admin.ModelAdmin):
    list_display = ("id", "create_time", "content")

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ("id", "update_time", "key", "total")

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "update_time", "title", "question_id", "url")