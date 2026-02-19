import re


class Normalise:
    @classmethod
    def normalise(cls, value):
        value = value.lower().strip()
        replacements = {
            'а': 'a',
            'б': 'b',
            'в': 'v',
            'г': 'g',
            'д': 'd',
            'е': 'e',
            'ё': 'e',
            'ж': 'z',
            'з': 'z',
            'и': 'i',
            'й': 'y',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'h',
            'о': 'o',
            'п': 'p',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'ф': 'f',
            'х': 'x',
            'ц': 's',
            'ч': 'h',
            'ш': 's',
            'щ': 'h',
            'ъ': '',
            'ы': 'y',
            'ь': '',
            'э': 'e',
            'ю': 'u',
            'я': 'y',
            'n': 'h',
        }
        for old, new in replacements.items():
            value = value.replace(old, new)
        value = re.sub(r'[^\w\s]', '', value)
        value = re.sub(r'\s+', '', value)
        value = re.sub(r'\d+', '', value)
        value = re.sub(r'(.)\1+', r'\1', value)
        return value.strip()
