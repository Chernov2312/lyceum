import re

from django.conf import settings


class ReverseRussianMiddleware:
    counter = 0
    russian_pattern = re.compile(r'[а-яА-ЯЁё]+')

    @classmethod
    def reverse_words(cls, response):
        content = response.content.decode('utf-8')
        russian_words = cls.russian_pattern.findall(content)
        text = [i[::-1] if i in russian_words else i for i in content.split()]
        response.content = ' '.join(text).encode()
        return response

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.ALLOW_REVERSE:
            ReverseRussianMiddleware.counter += 1
            if (
                ReverseRussianMiddleware.counter
                % settings.REQUESTS_COUNT_BEFORE_REVERSE
                == 0
            ):
                response = ReverseRussianMiddleware.reverse_words(response)
                ReverseRussianMiddleware.counter = 0
        return response
