import re

import django.core.validators


def validate_words_in_text(value: str):
    words_need = ['превосходно', 'роскошно']
    pattern = r'\b(?:' + '|'.join(words_need) + r')\b'
    must_be_word = re.compile(pattern, flags=re.IGNORECASE)
    if not must_be_word.search(value):
        raise django.core.validators.ValidationError(
            f'Обязательно нужно использовать одно из слов {words_need}',
        )
    return value
