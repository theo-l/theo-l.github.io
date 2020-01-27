from api_register_demo4 import Application, MockRequest, client




# A parameter validation decorator
def required_field(fields:list=None):
    def view_decorator(endpoint):
        def wrapped(request):
            payload = request.payload or {}
            missing_required_fields = set(fields)-set(payload.keys())
            if missing_required_fields:
                return {'status':422, 'message':f'Required fields: {missing_required_fields} are missing'}
            return endpoint(request)
        return wrapped
    return view_decorator


app = Application()

@app.post('/truckpaders')
@required_field(['name'])
def create_truckpader(request:MockRequest):
    return {'status':201, 'message':'create truckpader success!'}


if __name__ == "__main__":
    create_request = MockRequest('/truckpaders', 'post')
    client(create_request)

    # NOTE 1: required fields needed
    # create_request.payload={'name':'liang'}
    # client(create_request)
