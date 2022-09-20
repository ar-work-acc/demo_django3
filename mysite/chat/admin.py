from django.contrib import admin

from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'text', 'created')
    list_display_links = ('from_user', 'to_user', 'text')
    list_filter = ('from_user', 'to_user')
    search_fields = ('from_user', 'to_user')
    readonly_fields = ('created',)
