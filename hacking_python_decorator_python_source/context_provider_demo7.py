from api_register_demo4 import Application, MockRequest, client


def error_handler(endpoint):  # decorator as context provider
    def wrapped(request: 'MockRequest'):
        try:
            return endpoint(request)
        except Exception as error:
            return {'status': 500, 'message': f'Server internal error:{str(error)}'}

    return wrapped


app = Application()


@app.post('/truckpaders_ok')
def create_truckpader_ok(request:MockRequest):
    return {'status':201, 'message':'create truckpader success!'}

@app.post('/truckpaders_fail')
@error_handler # NOTE 1 error 
def create_truckpader_fail(request:MockRequest):
    return {'status':201, message:'create truckpader success!'}


if __name__ == "__main__":
    create_ok_request = MockRequest('/truckpaders_ok', 'post')
    client(create_ok_request)

    create_fail_request = MockRequest('/truckpaders_fail', 'post')
    client(create_fail_request)
