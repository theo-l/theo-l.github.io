class Employee:
    def __init__(self, name=None, profession=None, salary=None, department=None):
        self.name, self.profession, self.salary, self.department = name, profession, salary, department


class EmployLevel:
    def __init__(self, salary):
        self.salary = salary


class Junior(EmployLevel):
    def __init__(self):
        super().__init__(2000)


class Full(EmployLevel):
    def __init__(self):
        super().__init__(3000)


class Senior(EmployLevel):
    def __init__(self):
        super().__init__(4000)


class BackendJunior(Employee, Junior):
    def __init__(self, name):
        Employee.__init__(self, name, profession='backend', department='engineer')
        Junior.__init__(self)


if __name__ == '__main__':
    alice = BackendJunior('alice')
    print('-'*60, '\n')
    print(f'<Employee: name={alice.name}, profession={alice.profession}, department={alice.department}, salary={alice.salary}>')
    print('\n', '-'*60)
