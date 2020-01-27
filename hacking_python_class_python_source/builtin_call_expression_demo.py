class CallableInstanceClass:

    def __init__(self, name):
        print(f'calling class:<{self.__class__.__name__}>')
        self.name = name

    def __call__(self, *args, **kwargs):
        print(f'calling instance:<{self.name}>')


if __name__ == '__main__':
    callable_instance = CallableInstanceClass('callable instance')
    callable_instance()
