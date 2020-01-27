# Create a decorator with function definition
def public_decorator_function(callable):
    callable.is_public = True
    return callable


# Create a decorator with class definition
class public_decorator_class:

    def __init__(self, callable):
        self.is_public = True
        self.callable = callable

    def __call__(self, *args, **kwargs):
        return self.callable(*args, **kwargs)


def non_public_function():  # method without marker decorator
    print('non public function')


@public_decorator_function
def function_public_marked_function():  # method marked by decorator function
    print('function public marked function')


@public_decorator_class
def class_public_marked_function():  # method marked by decorator class
    print('class public marked function')


# helper to mock 'is_public' mark check
def request(callable):
    if not getattr(callable, 'is_public', False):
        print('Non public callable object is not allowed!')
        return
    callable()


if __name__ == '__main__':
    request(function_public_marked_function)
    request(class_public_marked_function)
    request(non_public_function)
