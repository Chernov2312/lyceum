import re

import django.core.validators


def validate_slug(value: str):
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise django.core.validators.ValidationError(
            'Слаг может содержать только латиницу, цифры,'
            'дефис и подчеркивание',
            params={'value': value},
        )
