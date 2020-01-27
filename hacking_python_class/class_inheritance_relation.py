class Employee:
    def __init__(self, name, salary=0):
        self.name = name
        self.salary = salary

    def work(self):
        return f'{self.name} does stuff'

    def raise_salary(self, percent):
        self.salary *= (1.0 + percent)

    def __repr__(self):
        return f'<Employee: name={self.name}, salaray={self.salary}>'


class Chef(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 5000)

    def work(self):
        print(f'{self.name} makes food')


class Server(Employee):
    def __init__(self, name):
        Employee.__init__(self, name, 4000)

    def work(self):
        print(f'{self.name} attend customer')


if __name__ == '__main__':
    bob = Chef('Bob')
    lucy = Server('Lucy')
