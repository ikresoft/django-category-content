#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.core.paginator import EmptyPage, InvalidPage
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.utils.encoding import force_unicode
from django.template.loader import find_template
from django.template.base import TemplateDoesNotExist

from content import settings
from content.views import ContentListView, ContentDetailView, ContentViewMixin
from models import CategoryContent

from categories.views import get_category_for_path


def get_sub_categories(self, category):
    qs = category.get_descendants()
    categories = [category.pk]
    for node in qs:
        categories.append(node.pk)
    return categories

class CategoryContentViewMixin(ContentViewMixin):

    def get_extra_data(self, **kwargs):
        extra_data = {}
        try:
            extra_data['category'] = get_category_for_path(self.kwargs["path"])
            self.category = extra_data['category']
        except:
            raise Http404

        return extra_data

    def _get_templates(self, name):
        opts = self.object.get_real_instance()._meta
        app_label = opts.app_label
        path = CategoryContent.get_path(self.category)
        return ["%s/%ss/%s/%s.html" % (app_label, opts.object_name.lower(), path, name)]

class CategoryContentListView(ContentListView, CategoryContentViewMixin):
    model = CategoryContent

    def get_queryset(self):
        qs = super(CategoryContentListView, self).get_queryset()
        return qs.filter(categories__in=get_sub_categories(self.category))


class CategoryContentDetailView(ContentDetailView, CategoryContentViewMixin):
    model = CategoryContent
