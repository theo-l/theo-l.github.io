from datetime import datetime
import time
from api_register_demo4 import Application, MockRequest, client


CACHER = {}

# Decorator for data cache usage
def cache(seconds=1000):  
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


app = Application()


@app.post('/truckpaders')
@cache(10)
def create_truckpader(request:MockRequest):
    time.sleep(3)
    return {'status':201, 'message':'create truckpader success!'}


if __name__ == "__main__":
    create_request = MockRequest('/truckpaders', 'post')
    client(create_request)
    client(create_request)
    time.sleep(10)
    client(create_request)

