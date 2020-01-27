def public_decorator(callable):
    callable.public = True
    return callable


def any_callable():
    pass


@public_decorator
def public_decorated_callable():
    pass


if __name__ == '__main__':
    print('true' if getattr(any_callable, 'public', False) else 'false')
    public_marked_callable = public_decorator(any_callable)
    print('true' if getattr(public_marked_callable, 'public', False) else 'false')
    print('true' if getattr(public_decorated_callable, 'public', False) else 'false')
