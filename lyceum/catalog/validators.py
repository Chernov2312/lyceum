import re

import django.core.validators
from django.utils.deconstruct import deconstructible


@deconstructible
class ValidateMustContain(django.core.validators.BaseValidator):
    def __init__(self, *words):
        self.words = words
        self.pattern = r'\b(?:' + '|'.join(self.words) + r')\b'
        self.message = (
            f'Обязательно нужно использовать одно из слов {self.words}'
        )

    def __call__(self, value):
        if not re.search(self.pattern, value, flags=re.IGNORECASE):
            raise django.core.validators.ValidationError(self.message)
