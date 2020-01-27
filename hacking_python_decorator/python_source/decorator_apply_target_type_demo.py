def function_mark_decorator(callable):
    callable.mark = 'function'
    return callable

def class_mark_decorator(klass):
    klass.mark = 'class'
    return klass

def method_mark_decorator(method):
    method.mark = 'function'
    return method

class function_only_mark_decorator_class:
    def __init__(self, func):
        self.func = func
        self.func.mark = 'function_only_mark_decorator_class'

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class compatible_function_and_method_decorator_class(function_only_mark_decorator_class):
    def __get__(self, instance, owner):
        return (lambda *args, **kwargs: self.func(instance, *args, **kwargs))

@function_mark_decorator
def function_callable():
    print(f'calling function callable object!')

@function_only_mark_decorator_class
def function_callable2():
    print(f'calling function callable with function_callable_with_function_only_mark_decorator_class')

@compatible_function_and_method_decorator_class
def function_callable3():
    print(f'calling function callable with compatible_function_and_method_decorator_class!')

@class_mark_decorator
class ClassCallable:

    def __init__(self):
        print('calling class callable object!')

    @method_mark_decorator
    def method_callable(self):
        print('calling method callable object!')

    @function_only_mark_decorator_class
    def method_callable2(self):
        print(f'calling method with function_only_mark_decorator_class')

    @compatible_function_and_method_decorator_class
    def method_callable3(self):
        print(f'calling method with compatible_function_and_method_decorator_class')

if __name__ == '__main__':
    function_callable()
    obj = ClassCallable()
    obj.method_callable()
    function_callable2()
    # obj.method_callable2()  # cause error
    function_callable3()
    obj.method_callable3()
