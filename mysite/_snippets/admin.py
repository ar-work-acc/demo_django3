from django.contrib import admin

from .models import Snippet


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'linenos', 'language', 'style', 'owner', 'user_name')
    list_display_links = ('title',)  # just a note
    list_editable = ('linenos',)
    list_filter = ('owner',)
    search_fields = ('title',)
    date_hierarchy = 'created'

    # fields = ('title', 'code', ('language', 'style'), 'linenos', 'owner')
    fieldsets = (
        (
            'Code', {
                'fields': ('title', 'code'),
            }
        ),
        (
            'Formatting options', {
                # 'classes': ('collapse',),
                'description': '(set code display style here)',
                'fields': (('language', 'style'), 'linenos',)
            }
        ),
        (
            'Author', {
                'fields': ('owner',)
            }
        )
    )

    exclude = ('highlighted',)  # automatically generated from code, so exclude it
    readonly_fields = ('owner',)  # snippet's owner shouldn't be modified

    @admin.display(description="Name", ordering='owner__first_name')
    def user_name(self, obj: Snippet) -> str:
        user = obj.owner
        return f'{user.first_name} {user.last_name}'
