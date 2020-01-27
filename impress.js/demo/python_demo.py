from collections import OrderedDict


class Employee:
    employee_count = 0
    employee_position_count = {}

    __private_value = 'private'

    _some_private_value = 'some private value'

    __slots__ = ['name', 'age', 'position', '_value']

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, name: str = None, age: int = 0, position: str = None):
        self.name = name
        self.age = age
        self.position = position

        Employee.employee_position_count.setdefault(position, 0)
        Employee.employee_position_count[position] += 1
        Employee.employee_count += 1
        self._value = 'test'

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def work(self):
        print(f'{self.name} is working now!')

    @classmethod
    def get_employee_count(cls):
        print(f'Total employee: {cls.employee_count}')

    @staticmethod
    def get_employee_position_count(position: str = None):
        if not position:
            print(f'Employee in {position}: {Employee.employee_position_count[position]}')
        print(f'Employee in {position}: {Employee.employee_position_count.get(position, 0)}')

    def __str__(self):
        return f'({self.name} : {self.age} : {self.position})'


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
        print(f'Before getting value of <{item}> in __getattr__')
        if item == 'age':
            return 25
        result = super(EmployeeAttributeDemo, self).__getattr__(item)
        print(f'After getting value of <{item}> in __getattr__ \n')
        return result

    def __getattribute__(self, item):
        print(f'Before getting value of <{item}> in __getattribute__')
        result = super(EmployeeAttributeDemo, self).__getattribute__(item)
        print(f'After getting value of <{item}> in __getattribute__\n')
        return result


if __name__ == '__main__':
    em = EmployeeAttributeDemo('original instance value')

    print(EmployeeAttributeDemo.__dict__.keys())

    # print(em.public_value)
    # em.public_value = 'another public value'
    # print(em.public_value)
    #
    # print(em._fake_private_value)
    # em._fake_private_value = 'another fake private value'
    # print(em._fake_private_value)
    #
    # print(em.name)
    # em.name = 'Sapo'
    # print(em.name)
    #
    # print(em.instance_value)
    # em.instance_value = 'new instance value'
    # print(em.instance_value)
    #
    # print(em.age)  # access non-exist attribute will call __getattribute__
    # em.age = 20
    # print(em.age)

    # print(em.__real_private_value)  # cause error
    # print(em._EmployeeAttributeDemo__real_private_value)  # cause error


