import modeltranslation 
from modeltranslation.translator import TranslationOptions, translator,register

from.models import *

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)