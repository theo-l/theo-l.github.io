import time
from datetime import datetime
from api_register_demo4 import Application, MockRequest, client


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
@api_tracker() # NOTE 1: track the call of endpoint
def create_truckpader(request: 'MockRequest'):
    time.sleep(1)  
    return {'status': 201, 'message': 'create truckpader success!'}

if __name__ == "__main__":
    create_requeset = MockRequest('/truckpaders', 'post')
    client(create_requeset)
