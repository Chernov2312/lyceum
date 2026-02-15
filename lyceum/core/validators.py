import re

import django.core.validators


def validate_slug(value: str):
    if not re.match(r'^[a-zA-Z0-9_-]+$', value):
        raise django.core.validators.ValidationError(
            'Слаг может содержать только латиницу, цифры,'
            'дефис и подчеркивание',
            params={'value': value},
        )


def validate_name(value: str):
    if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
        raise django.core.validators.ValidationError(
            'Название не может быть числом',
        )
    if not re.match(r'^[а-яА-ЯёЁa-zA-Z0-9\s-]+$', value):
        raise django.core.validators.ValidationError(
            'Название содержит недопустимые символы',
        )

    return value
