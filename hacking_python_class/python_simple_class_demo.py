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


if __name__ == '__main__':
    em1 = Employee('alice', 20, 'back')
    # em2 = Employee('bob', 22, 'front')
    # em3 = Employee('cici', 21, 'iOS')
    #
    # Employee.get_employee_count()  # calling a class method
    # Employee.get_employee_position_count('back')  # calling a static method
    #
    # print(em1)
    # print(em1.value)
    # em1.value = 'setted value'
    # print(em1.value)
    # print(Employee._some_private_value)
