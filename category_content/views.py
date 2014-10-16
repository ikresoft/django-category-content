#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from content.views import ContentListView, ContentDetailView, ContentViewMixin
from models import CategoryContent

from categories.views import get_category_for_path


def get_sub_categories(category):
    qs = category.get_descendants()
    categories = [category.pk]
    for node in qs:
        categories.append(node.pk)
    return categories


class CategoryContentViewMixin(ContentViewMixin):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'category'):
            try:
                self.category = get_category_for_path(self.kwargs["path"])
            except:
                raise Http404
        return super(CategoryContentViewMixin, self).dispatch(request, *args, **kwargs)

    def get_extra_data(self, **kwargs):
        extra_data = {}
        extra_data['category'] = self.category
        return extra_data

    def _get_templates(self, name):
        opts = self.model._meta
        app_label = opts.app_label
        path = CategoryContent.get_path(self.category)
        return ["%s/%ss/%s/%s.html" % (app_label, opts.object_name.lower(), path, name)]


class CategoryContentListView(CategoryContentViewMixin, ContentListView):
    model = CategoryContent

    def get_context_data(self, **kwargs):
        context = super(CategoryContentListView, self).get_context_data(**kwargs)

        paginator = Paginator(self.qs, settings.POSTS_PER_PAGE)
        page = self.request.GET.get("page")
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context['object_list'] = posts
        return context

    def get_queryset(self):
        qs = super(CategoryContentListView, self).get_queryset()
        self.qs = qs.filter(categories__in=get_sub_categories(self.category))

        return qs


class CategoryContentDetailView(CategoryContentViewMixin, ContentDetailView):
    model = CategoryContent
