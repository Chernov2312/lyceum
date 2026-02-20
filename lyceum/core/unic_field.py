import re


class Normalise:
    @classmethod
    def normalise(cls, value):
        value = value.strip()
        replacements = {
            'З': '',
            'а': 'a',
            'в': 'b',
            'е': 'e',
            'ё': 'e',
            'к': 'k',
            'м': 'm',
            'н': 'h',
            'о': 'o',
            'р': 'p',
            'с': 'c',
            'т': 't',
            'у': 'y',
            'х': 'x',
            'А': 'a',
            'В': 'b',
            'Е': 'e',
            'Ё': 'e',
            'К': 'k',
            'М': 'm',
            'Н': 'h',
            'О': 'o',
            'Р': 'p',
            'С': 'c',
            'Т': 't',
            'У': 'y',
            'Х': 'x',
            'l': 'I',
            'ь': 'b',
            'ъ': 'd',
        }
        for old, new in replacements.items():
            value = value.replace(old, new)
        value = re.sub(r'[^\w\s]', '', value.lower())
        value = re.sub(r'\s+', '', value)
        value = re.sub(r'\d+', '', value)
        value = re.sub(r'(.)\1+', r'\1', value)
        return value.strip()
