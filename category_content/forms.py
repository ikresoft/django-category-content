from django import forms
from content.forms import ContentForm
from models import CategoryContent
from categories.models import Category
from widgets import MpttTreeWidget

class CategoryContentForm(ContentForm):
	categories = forms.ModelMultipleChoiceField(required=True, queryset=Category.objects.all(), widget=MpttTreeWidget)

	class Meta:
		model = CategoryContent
