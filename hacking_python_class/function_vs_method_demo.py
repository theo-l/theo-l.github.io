def plain_hello(name: str = None):  # when bound to class, name is going to be treated as self
    print(f'Hello, {name or "World"}')


def unbindable_hello():
    print('Hello, unbindable function')


def bindable_hello(mock_self, name: str = None):
    print(f'Hello, {mock_self.name or name}')


class Hello:
    def __init__(self, name):
        self.name = name or 'World'

    def __call__(self, *args, **kwargs):
        return f'Instance : {self.name}'


if __name__ == '__main__':
    name = 'function vs method'
    plain_hello(name)  # function call

    Hello.hello = bindable_hello
    obj = Hello(name)  # class call
    obj.hello()  # method call

    Hello.hello = plain_hello
    obj = Hello(name)
    obj.hello()

    Hello.hello = unbindable_hello
    obj = Hello(name)
    obj.hello()

    print(obj())  # instance call
