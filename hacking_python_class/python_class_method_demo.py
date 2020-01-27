class Hello:
    instance_count = 0

    def __init__(self, name: str = None):
        self.name = name
        Hello.instance_count += 1

    @classmethod
    def children(cls):
        return cls.instance_count

    @staticmethod
    def greeting(name: str = None):
        return f'Hello, static: {name or "World"}!'

    def hello(self, name: str = None):
        return f'Hello, instance: {name or self.name}!'

    def __str__(self):
        return f'Hello, {self.name}!'


if __name__ == '__main__':
    obj1 = Hello('obj1')
    obj2 = Hello('obj2')

    # Class method invocation
    print(Hello.children())

    # Static method invocation with both class & instance
    print(Hello.greeting('Class greeting'))
    print(obj1.greeting('Instance greeting'))

    # Instance method invocation with both class & instance
    print(Hello.hello(obj1))
    print(obj1.hello())

    # Class builtin method invocation with instance implicitly
    print(obj1)
    print(obj2)
