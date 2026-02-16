import re

import django.core.validators
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _


@deconstructible
class ValidateMustContain(django.core.validators.BaseValidator):
    def __init__(self, words):
        self.words = words
        self.pattern = r'\b(?:' + '|'.join(words) + r')\b'
        self.message = _(f'Обязательно нужно использовать одно из слов {words}')
    
    def __call__(self, value):
        print(value)
        if not re.search(self.pattern, value, flags=re.IGNORECASE):
            raise django.core.validators.ValidationError(self.message)