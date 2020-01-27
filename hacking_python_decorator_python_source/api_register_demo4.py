class Application:
    APPLICATION = {}

    def _route(self, url: str, method: str):
        def register_decorator(callback):
            prefix = f'{url.upper()}-{method.upper()}'
            Application.APPLICATION[prefix] = callback
            return callback

        return register_decorator

    def get(self, url):
        return self._route(url, 'get')

    def post(self, url):
        return self._route(url, 'post')


class MockRequest:
    def __init__(self, url, method, payload=None, headers=None):
        self.url = url
        self.method = method
        self.payload = payload or {}
        self.headers = headers or {}
        self.prefix = f'{url.upper()}-{method.upper()}'


def client(request):
    if request.prefix not in Application.APPLICATION:
        return {'status':405, 'message': f'Method: {request.method.upper()} not allowed in url: {request.url.upper()}'}
    print(Application.APPLICATION[request.prefix](request), end=f'\n{"-"*60}\n')


app = Application()

@app.post('/truckpaders')
def create_truckpader(request:MockRequest):
    return {'status':201, 'message':'create truckpader success!'}

if __name__ == "__main__":
    create_request = MockRequest('/truckpaders', 'post')
    client(create_request)
