def decorator_function(callable):
    callable.decorator_type = 'function'
    return callable

class decorator_class:

    def __init__(self, callable=None):
        if callable:
            self.callable = callable
            self.decorator_type = 'class'

    def decorator_method(self, callable):
        callable.decorator_type ='method'
        return callable

    def __call__(self, callable):
        callable.decorator_type = 'instance'
        return callable


@decorator_function
def function_decorated():
    pass

@decorator_class
def class_decorated():
    pass

instance= decorator_class()

@instance.decorator_method
def method_decorated():
    pass

@instance
def instance_decorated():
    pass

def decorator_type_detector(callable):
    print(f'Callable: <{getattr(callable,"__name__",callable.__class__.__name__ )}> decorator type: <{getattr(callable, "decorator_type", "unknow decorator type").upper()}>')


if __name__ == "__main__":
    decorator_type_detector(function_decorated)
    decorator_type_detector(class_decorated)
    decorator_type_detector(method_decorated)
    decorator_type_detector(instance_decorated)
    

