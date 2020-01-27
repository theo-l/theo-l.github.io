import types
def general_decorator(obj):
    if isinstance(obj, type):
        obj.applied_to = 'class'
    if isinstance(obj, types.FunctionType):
        if 'function' in obj.__name__:
            obj.applied_to = 'function'
        elif 'method' in obj.__name__:
            obj.applied_to = 'method'
        elif obj.__name__ == '__call__':
            obj.applied_to = 'instance'
    return obj 

@general_decorator
def decorated_function():pass
@general_decorator
class decorated_class():
    @general_decorator
    def decorated_method():pass
    @general_decorator
    def __call__(self, *args, **kwargs):
        self.decorated_instance()

def detect_decorator_place(obj):
    print(f'Decorator applied to <{getattr(obj, "applied_to").upper()}>:[{obj.__name__}]')

if __name__ == "__main__":
    detect_decorator_place(decorated_function)
    detect_decorator_place(decorated_class)
    detect_decorator_place(decorated_class.decorated_method)
    detect_decorator_place(decorated_class.__call__)


