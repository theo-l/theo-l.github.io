import types
def general_decorator(obj):
    if isinstance(obj, type):
        obj.decoration_type = 'CLASS'
    if isinstance(obj, types.FunctionType):
        if obj.__name__ == '__call__':
            obj.decoration_type = 'INSTANCE'
        elif 'function' in obj.__name__:
            obj.decoration_type = 'FUNCTION'
        elif 'method' in obj.__name__ :
            obj.decoration_type = 'METHOD'
        else:
            obj.decoration_type = 'UNKNOWN'

    return obj


@general_decorator
class Demo:
    def __init__(self):
        pass

    @general_decorator
    def method(self):
        pass

    @general_decorator
    def __call__(self):
        pass

@general_decorator
def function():
    pass

if __name__ == "__main__":
    for obj in [Demo, Demo.method, Demo.__call__, function]:
        print(getattr(obj, 'decoration_type', 'UNKNOWN'))
