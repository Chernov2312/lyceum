from django.http import HttpResponse


class MiddlewareCounter:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):
        response = self.get_response(request)
        self.counter += 1
        if self.counter == 10:
            text = [i[::-1] for i in response.text.split()]
            self.counter = 0
            response = HttpResponse(
                ' '.join(text), content_type='text/plain; charset=utf-8'
            )
        return response
