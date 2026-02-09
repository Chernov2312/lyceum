from django.conf import settings


class MiddlewareCounter:
    counter = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if settings.ALLOW_REVERSE:
            MiddlewareCounter.counter += 1
            if MiddlewareCounter.counter % 10 == 0:
                content = response.content.decode('utf-8')
                text = [i[::-1] for i in content.split()]
                MiddlewareCounter.counter = 0
                response.content = ' '.join(text).encode()
        return response
