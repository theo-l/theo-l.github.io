class DescriptorAttr:
    def __init__(self, value=None):
        self._value = value

    def __get__(self, instance, klass):
        return self._value

    def __set__(self, instance, value):
        self._value = value


class Employee(object):
    public_attr = 'public value'
    _fake_private_attr = 'fake private value'
    __private_attr = 'not really private value'
    descriptor_attr = DescriptorAttr('descriptor value')

    def __init__(self, name=None):
        self.name = name


if __name__ == '__main__':
    alice = Employee('alice')
    print(alice.name, end='\n')
    print(alice.public_attr, end='\n')
    print(alice._fake_private_attr, end='\n')
    print(alice.descriptor_attr, end='\n')
    # print(alice.__private_attr, end='\n') # cause error
    print(alice._Employee__private_attr, end='\n') # cause error
