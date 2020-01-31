from copy import copy
class Pizza:
    def __init__(self, data, muiltple=True):
        print(f'\nCreated an Iterable object <{type(data).__name__.upper()} pizza>!\n')
        self.data = data
        self.muiltple=muiltple

    def __iter__(self):
        print('<Using iteration protocol method!>\n')
        print('<waiter serve>:', end='')
        self.ix = 0
        if self.muiltple:
            return copy(self)
        return self

    def __next__(self):
        print('<next piece>:', end='')
        if self.ix >= len(self.data):
            raise StopIteration('Pizza is finished')
        result = self.data[self.ix]
        self.ix += 1
        return result


class Waiter:

    def __init__(self, pizza:Pizza):
        print('Trying to convert an Iterable object to Iterator!\n')
        self.pizza = iter(pizza)

    def next(self):
        return next(self.pizza)
    
class Pizzaeria:
    
    @classmethod
    def make_list_pizza(cls):
        pizza = Pizza([1,2,3,4,5])
        return cls.serve(pizza)

    @classmethod
    def make_tuple_pizza(cls):
        pizza = Pizza((1,2,3,4,5,6))
        return cls.serve(pizza)


    @classmethod
    def serve(cls, pizza):
        print('Calling in Iteration context <PIZZAERIA>!\n')
        return Waiter(pizza)

class Client:
    
    @staticmethod
    def order_pizza(pizza_type):
        return pizza_type

    @staticmethod
    def ask_pizza(waiter:Waiter):
        return waiter.next()


if __name__ == "__main__":
    liang = Client()
    pizza_type = liang.order_pizza('list')
    pizza = Pizzaeria.make_list_pizza() # call directly
    try:
        liang.ask_pizza(pizza)
        liang.ask_pizza(pizza)
        liang.ask_pizza(pizza)
        liang.ask_pizza(pizza)
        liang.ask_pizza(pizza)
        liang.ask_pizza(pizza)
        liang.ask_pizza(pizza)
    except StopIteration as e:
        print(f'\n{"="*40}\n{e}\n')








