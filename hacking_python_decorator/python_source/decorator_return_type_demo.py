# decorator which return the original object
def simple_marker_decorator(callable):
    callable.mark = 'simple'
    return callable


# decorator wrapped the original object and return the wrapper
def wrapped_marker_decorator(callable):
    def wrapper(*args, **kwargs):
        print(f'origin callable:{callable}')
        return callable(*args, **kwargs)

    wrapper.mark = 'wrapped'

    return wrapper


def func1():
    print('Calling fun1')


def func2():
    print('Calling fun2')


if __name__ == '__main__':
    print(func1)
    # here is the same as
    # @simple_marker_decorator
    # def func1():
    #    ...
    func1 = simple_marker_decorator(func1)
    print(func1)

    print(func2)
    # here is the same as
    # @wrapped_marker_decorator
    # def func2():
    #    ...
    func2 = wrapped_marker_decorator(func2)
    print(func2)
