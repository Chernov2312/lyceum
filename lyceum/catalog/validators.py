import re

import django.core.validators


def validate_words_in_text(value: str):
    words_need = ['превосходно', 'роскошно']
    pattern = '|'.join(f'({word})' for word in words_need)
    must_be_word = re.compile(pattern, flags=re.IGNORECASE)
    if not must_be_word.findall(value):
        raise django.core.validators.ValidationError(
            f'Обязательно нужно использовать одно из слов {words_need}'
        )
    return value
