from django.contrib import admin

from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "slug")
    prepopulated_fields = {"slug": ("title", )}


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("user", "content", "date")


class TagsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("tag_name",)}


admin.site.register(Tags, TagsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comments, CommentsAdmin)

