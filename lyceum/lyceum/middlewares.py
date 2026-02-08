class MiddlewareCounter:
    def __init__(self, get_response):
        self.get_response = get_response
        self.counter = 0

    def __call__(self, request):
        response = self.get_response(request)
        self.counter += 1
        return response
