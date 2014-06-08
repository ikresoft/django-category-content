from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content.admin import ChildAdmin
from forms import CategoryContentForm
from models import CategoryContent

from content import settings

class CategoryContentAdmin(ChildAdmin):
    base_model = CategoryContent
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
            'fields': ('title', 'body')
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
