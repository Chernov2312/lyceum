import re


class Normalise:
    @classmethod
    def normalize(cls, value):
        value = value.lower().strip()
        replacements = {
            'а': 'a',
            'с': 'c',
            'е': 'e',
            'о': 'o',
            'р': 'p',
            'х': 'x',
            'у': 'y',
            'в': 'b',
            'н': 'h',
            'к': 'k',
            'т': 't',
            'м': 'm',
            'и': 'u',
            'ё': 'e',
            'й': 'i',
            'ъ': '',
            'ь': '',
        }
        for old, new in replacements.items():
            value = value.replace(old, new)
        value = re.sub(r'[^\w\s]', '', value)
        value = re.sub(r'\s+', ' ', value)
        return value.strip()
