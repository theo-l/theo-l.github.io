class_parents = (object,)
class_name = 'Employee'

class_attributes = {'name': None, 'salary': 0}


def bindable_work(self):
    print(f'{self.name} is working!')


def customized_init(self, name, salary=0):
    self.name = name
    self.salary = salary


def customized_raise_salary(self, percent):
    self.salary *= (1.0 + percent)


def customized_str(self):
    return f'<{class_name}: name={self.name}, salary={self.salary}>'


class_methods = {
    '__init__': customized_init,
    'work': bindable_work,
    'raise_salary': customized_raise_salary,
    '__str__': customized_str
}

Employee = type(class_name, class_parents, {**class_attributes, **class_methods})

if __name__ == '__main__':
    bob = Employee('Bob', 2000)
    print(bob)
    bob.work()
    bob.raise_salary(0.2)
    print(bob)
