import time
from datetime import datetime
CACHER = {}


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


def required_field(fields: list = None):  # decorator as data validation
    def view_decorator(endpoint):
        def wrapped(request):
            payload = request.payload or {}
            missing_required_fields = set(fields) - set(payload.keys())
            if missing_required_fields:
                return {'status': 422, 'message': f'Required fields: {missing_required_fields} are missing'}
            return endpoint(request)

        return wrapped

    return view_decorator


def cache(seconds=1000):  # decorator as data cacher
    def view_decorator(endpoint):
        def wrapped(request: 'MockRequest'):
            global CACHER
            if request.prefix in CACHER:
                delta = datetime.now() - CACHER[request.prefix]['cache_time']
                if delta.total_seconds() <= seconds:
                    print('Fetching result from cache')
                    return CACHER[request.prefix]['result']
            print('Reset cache value!')
            result = endpoint(request)
            CACHER[request.prefix] = {'result': result, 'cache_time': datetime.now()}
            return result

        return wrapped

    return view_decorator


def error_handler(endpoint):  # decorator as context provider
    def wrapped(request: 'MockRequest'):
        try:
            return endpoint(request)
        except Exception as error:
            return {'status': 500, 'message': f'Server internal error:{str(error)}'}

    return wrapped


def api_tracker(time=True):
    def view_decorator(endpoint):
        def wrapped(request: 'MockRequest'):
            if time: start = datetime.now()
            print('--------Before api call')
            result = endpoint(request)
            if time: end = datetime.now()
            print(f'----target result:{result}')
            print(f'--------After api call {(end-start).total_seconds() if time else ""}')
            return result

        return wrapped

    return view_decorator


app = Application()


@app.post('/truckpaders')
# @required_field(['name']) # NOTE 1: parameter validation
# @cache(10) # NOTE 2: cache value
# @error_handler # NOTE 4: context provider
@api_tracker()  # NOTE 5: api track
def create_truckpader(request: 'MockRequest'):
    time.sleep(2)  # NOTE 5: api track
    return {'status': 201, 'message': 'create truckpader success!'}
    # raise ValueError('Error in api call') # NOTE 3: context provider demo


class MockRequest:
    def __init__(self, url, method, payload, headers):
        self.url = url
        self.method = method
        self.payload = payload
        self.headers = headers
        self.prefix = f'{url.upper()}-{method.upper()}'


def client(request):
    if request.prefix not in Application.APPLICATION:
        return {'status': 405, 'message': f'Method: {request.method.upper()} not allowed in url: {request.url.upper()}'}
    print(Application.APPLICATION[request.prefix](request), end=f'\n{"-"*60}\n')


if __name__ == "__main__":
    simple_create_truckpader_request = MockRequest('/truckpaders', 'post', {}, {})
    client(simple_create_truckpader_request)
    # simple_create_truckpader_request.payload = {'name':'liang'}
    # client(simple_create_truckpader_request)
    # time.sleep(10)
    # client(simple_create_truckpader_request)
