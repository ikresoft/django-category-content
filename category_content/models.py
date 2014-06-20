from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import force_unicode
from categories.fields import CategoryM2MField
from content.models import Content

from django.utils.translation import ugettext as _

class CategoryContent(Content):
    categories = CategoryM2MField(null=True, blank=True)
    allow_pings = models.BooleanField(_('Allow pings'), default=True)
    is_sticky = models.BooleanField(default=False)

    @classmethod
    def get_path(cls, category):
        ancestors = list(category.get_ancestors()) + [category, ]
        path = '/'.join([force_unicode(i.slug) for i in ancestors])
        return path

    def get_absolute_url(self, category=None):
        if self.category is None:
            category = self.categories.all()[0]
        return reverse('category_content_detail', args=[CategoryContent.get_path(category), self.slug])
