class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'<Employee: {self.name}>'

if __name__ == '__main__':
    a = Employee('alice')
    print(a)
