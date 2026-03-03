import re

from django.conf import settings

__all__ = ['ReverseRussianMiddleware']


class ReverseRussianMiddleware:
    counter = 0
    russian_pattern = re.compile(r'[а-яА-ЯЁё]+')

    @classmethod
    def replace_with_regex(cls, content):
        return re.sub(
            cls.russian_pattern,
            lambda m: m.group()[::-1],
            content,
        )

    @classmethod
    def reverse_words(cls, response):
        content = response.content.decode(response.charset)
        reversed_content = cls.replace_with_regex(content)
        response.content = reversed_content.encode(response.charset)
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
                return ReverseRussianMiddleware.reverse_words(response)

        return response
