from talks.hacking_python_class.class_inheritance_relation import Server, Chef


class Customer:
    def __init__(self, name):
        self.name = name

    def order(self, server):
        print(f'Client <{self.name}> orders from {server}')
        server.work()

    def pay(self, server):
        print(f'Client <{self.name}> pays for item to {server}')
        server.work()


class Oven:
    def bake(self):
        print('oven bakes')


class PizzaShop:
    def __init__(self):
        self.server = Server('Pat')
        self.chef = Chef('Bob')
        self.oven = Oven()

    def order(self, name):
        customer = Customer(name)
        customer.order(self.server)
        self.chef.work()
        self.oven.bake()
        customer.pay(self.server)


if __name__ == '__main__':
    tp_pizza = PizzaShop()
    tp_pizza.order('Python')
