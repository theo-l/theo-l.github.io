class NameDescriptor:
    def __init__(self, value):
        print(f'Before init descriptor attribute value: {value}')
        self._value = value
        print(f'After init descriptor attribute value: {value}\n')

    def __get__(self, instance, klass):
        print(f'Before getting attribute in descriptor: <{self.__class__.__name__}>.__get__')
        result = self._value
        print(f'After getting attribute in descriptor: <{self.__class__.__name__}>.__get__\n')
        return result

    def __set__(self, instance, value):
        print(f'Before setting attribute in descriptor: <{self.__class__.__name__}>.__set__')
        self._value = value
        print(f'After setting attribute in descriptor: <{self.__class__.__name__}>.__set__\n')


class EmployeeAttributeDemo:
    public_value = 'public'
    _fake_private_value = 'fake private value'  # python convention private attribute
    __real_private_value = 'not really a private value'  # real private attribute(which is not really private)

    name = NameDescriptor('alice')

    def __init__(self, instance_value):
        self.instance_value = instance_value

    def __setattr__(self, key, value):
        print(f'Before setting value of <{key}> => <{value}> in __setattr__')
        super(EmployeeAttributeDemo, self).__setattr__(key, value)
        print(f'After setting value of <{key}> => <{value}> in __setattr__ \n')

    # when access a non-exist attribute will be call
    def __getattr__(self, item):
        # avoid default invocation
        if item == '__len__':
            return super(EmployeeAttributeDemo, self).__getattr__(item)

        print(f'Before getting value of <{item}> in __getattr__')
        if item == 'age':
            return 25
        result = super(EmployeeAttributeDemo, self).__getattr__(item)
        print(f'After getting value of <{item}> in __getattr__ \n')
        return result

    def __getattribute__(self, item):
        if not item.startswith('__'):
            print(f'Before getting value of <{item}> in __getattribute__')
        result = super(EmployeeAttributeDemo, self).__getattribute__(item)
        if not item.startswith('__'):
            print(f'After getting value of <{item}> in __getattribute__\n')
        return result


if __name__ == '__main__':
    # em = EmployeeAttributeDemo('original instance value')


    def check_attribute_access(obj, attribute, new_value=None):
        print(getattr(obj, attribute))
        setattr(obj, attribute, new_value)
        print(getattr(obj, attribute))


    # check_attribute_access(obj, 'public_value', 'another public value')
    # check_attribute_access(obj, '_fake_private_value', 'another fake private value')
    # check_attribute_access(obj, 'name', 'new descriptor attribute value')
    # check_attribute_access(obj, 'instance_value', 'new instance value')
    # check_attribute_access(obj, 'age', 20)

    # print(em.__real_private_value)  # cause error
    # print(em._EmployeeAttributeDemo__real_private_value)  # cause error
