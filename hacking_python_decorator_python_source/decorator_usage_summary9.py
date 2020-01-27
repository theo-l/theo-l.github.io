import time
from api_register_demo4 import Application, MockRequest, client
from parameter_validation_demo5 import required_field
from data_cache_demo6 import cache
from context_provider_demo7 import error_handler
from api_tracker_demo8 import api_tracker



app = Application()

@app.post('/truckpaders')
@required_field(['name'])
# @cache(10) # will intercept every calls during the expiration period
@api_tracker() # the order of decorators matters
@error_handler
def create_truckpader(request:MockRequest):
    time.sleep(1)
    if getattr(request, 'error', False):
        raise ValueError('Test context provider decorator!')
    return {'status':201, 'message':'create truckpader success'}


if __name__ == "__main__":
    create_request = MockRequest('/truckpaders', 'post')
    client(create_request) # 422

    create_request.payload = {'name':'liang'}
    client(create_request) # 201

    create_request.error=True
    client(create_request) # 500

    create_request.error=False
    client(create_request)

