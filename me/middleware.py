from django.http import HttpResponse

class CountRequestMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        self.request_counter = 0
        self.exception_counter = 0

    def __call__(self, request):
        self.request_counter += 1
        print(f'This is request number {self.request_counter}')
        return self.get_response(request)

    def process_exception(self, request, exception):
        self.exception_counter += 1
        print(f'There was an exception {exception}\nThis in an exception number {self.exception_counter}')
        return HttpResponse(f'<html><body><h1>ох всё пропало!</h1><br>{exception}</body></html>')
