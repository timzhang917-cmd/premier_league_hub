from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "team", "author", "created_at")
    list_filter = ("team",)
    search_fields = ("title", "content", "author__username", "team__name")
    ordering = ("-created_at",)
