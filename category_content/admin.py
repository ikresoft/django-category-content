from django.utils.translation import ugettext_lazy as _

from content.admin import ContentAdmin
from forms import CategoryContentForm


class CategoryContentAdmin(ContentAdmin):
    quick_editable = (
        'title',
        'slug',
        'password',
        'private',
        'categories',
        'tags',
    )
    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        (_('Content'), {
            'fields': ('body',),
            'classes': ('full-width',),
        }),
        ('Categories', {
            'fields': ('categories',),
        }),
        (_('Post data'), {
            'fields': ('authors', 'non_staff_author',
                       'status', 'origin', 'allow_comments', 'allow_pings', 'is_sticky')
        }),)

    fieldsets = fieldsets + ((_('Advanced Options'), {
            'fields': ('slug', 'date_modified', 'site', ),
            'classes': ('collapse',),
        }),)
    form = CategoryContentForm
