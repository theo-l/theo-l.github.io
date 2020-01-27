def red_decorator(callable):
    callable.color = 'red'
    return callable


def green_decorator(callable):
    callable.color = 'green'
    return callable


def color_decorator(color):
    def dynamic_color_decorator(callable):
        callable.color = f'<{color.upper()}>'
        return callable

    return dynamic_color_decorator


def tracer_decorator(callable):
    def wrapper(*args, **kwargs):
        mark = '====>'
        print(f'{mark}Before calling method')
        result = callable(*args, **kwargs)
        print(f'{mark}After calling method')
        return result

    return wrapper


def labeled_tracer(label):
    def tracer_decorator(callable):
        def wrapper(*args, **kwargs):
            print(f'{label}Before calling method!')
            result = callable(*args, **kwargs)
            print(f'{label}After calling method!\n')
            return result

        return wrapper

    return tracer_decorator


@red_decorator
def static_red_callable():
    print('static red callable')


@green_decorator
def static_green_callable():
    print('static green callable')


@color_decorator('red')
def dynamic_red_callable():
    print('dynamic red callable')


@color_decorator('green')
def dynamic_green_callable():
    print('dynamic green callable')


def check_color(callable):
    print(f'Color of callable is: {getattr(callable, "color", None)}')


@tracer_decorator
def tracked_callable():
    print('Tracked callable object')


@labeled_tracer('####>')
def label_tracked_callable1():
    print('Label tracked callable object 1')


@labeled_tracer('@@@@>')
def label_tracked_callable2():
    print('Label tracked callable object 2')


if __name__ == '__main__':
    check_color(static_red_callable)
    check_color(static_green_callable)

    check_color(dynamic_red_callable)
    check_color(dynamic_green_callable)

    tracked_callable()
    label_tracked_callable1()
    label_tracked_callable2()
