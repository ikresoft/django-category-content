from modeltranslation.translator import translator, TranslationOptions
from models import CategoryContent

class CategoryContentTranslationOptions(TranslationOptions):
    pass

translator.register(CategoryContent, CategoryContentTranslationOptions)
