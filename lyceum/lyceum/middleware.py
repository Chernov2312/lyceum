class MiddlewareCounter:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):
        response = self.get_response(request)
        self.counter += 1
        if self.counter % 10 == 0:
            content = response.content.decode('utf-8')
            text = [i[::-1] for i in content.split()]
            self.counter = 0
            response.content = ' '.join(text).encode()
        return response
