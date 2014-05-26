from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content.admin import ChildAdmin
from forms import CategoryContentForm
from models import CategoryContent

from content import settings

class CategoryContentAdmin(ChildAdmin):
    base_model = CategoryContent
    fieldsets = (
        (None, {
            'fields': ('title', 'subhead', 'tease_title',
                       'teaser', 'body')
        }),
        ('Categories', {
            'fields': ('categories',),
        }),
        (_('Post data'), {
            'fields': ('authors', 'non_staff_author',
                       'status', 'origin', 'comment_status', )
        }),)

    if settings.INCLUDE_PRINT:
        fieldsets = fieldsets + (_('Print Information'), {
            'fields': ('print_pub_date', 'print_section', 'print_page'),
            'classes': ('collapse',),
        })

    fieldsets = fieldsets + ((_('Advanced Options'), {
            'fields': ('slug', 'date_modified', 'site', ),
            'classes': ('collapse',),
        }),)
    form = CategoryContentForm
