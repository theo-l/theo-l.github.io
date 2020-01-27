class Meta(type):
    def __getattribute__(self, item):
        print(f'>>>>>>>>Access class attribute: {item} in Meta.__getattribute__!\n')
        return super(Meta, self).__getattribute__(item)

    def __getattr__(self, item):
        print(f'>>>>>>>>Access class attribute: {item} in Meta.__getattr__!\n')
        return 25 if item == 'age' else super(Meta, self).__getattr__(item)

    def __setattr__(self, key, value):
        print(f'>>>>>>>>Set class attribute: <{key}> = <{value}> in Meta.__setattr__!\n')
        super(Meta, self).__setattr__(key, value)


class Employee(metaclass=Meta):
    count = 0

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    def __getattribute__(self, item):
        print(f'--------Access instance attribute: <{item}> in Employee.__getattribute__!\n')
        return super(Employee, self).__getattribute__(item)

    def __getattr__(self, item):
        print(f'--------Access instance attribute: {item} in Employee.__getattr__!\n')
        return 25 if item == 'age' else super(Employee, self).__getattr__(item)

    def __setattr__(self, key, value):
        print(f'--------Set instance attribute: <{key}>=<{value}> in Employee.__setattr__!\n')
        super(Employee, self).__setattr__(key, value)


if __name__ == '__main__':
    alice = Employee('alice')  # invoke instance and class attribute in __init__ method

    # print(alice.name)  # check access instance's initiated attribute process
    # print(alice.count)  # check access instance's class's attribute process
    # print(Employee.count)  # check access class's initiated attribute process

    # print(Employee.age)  # check access class's non-initiated attribute process
    # print(alice.age)  # check access instance's non-initiated attribute process
    # alice.hello()
