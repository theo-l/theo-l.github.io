class Employee:
    count = 0
    def __init__(self,name,position):
        self.name = name 
        self.position = position
        Employee.count += 1
    def work(self):
        pass
class Android(Employee):
    def __init__(self, name):
        super().__init__(name, 'android')
    def work(self):
        print(f'{self.name} is doing some KJ')
class Frontend(Employee):
    def __init__(self, name):
        super().__init__(name, 'frontend')
    def work(self):
        print(f'{self.name} is doing some HCJ')
class Backend(Employee):
    def __init__(self, name):
        super().__init__(name, 'backend')
    def work(self):
        print(f'{self.name} is doing some PR')


class Service:
    def work(self, truckpaders:list=None):
        for truckpader in truckpaders:
            truckpader.work()

if __name__ == '__main__':
    liang = Backend('liang')
    parazinho = Android('parazinho')
    paulinha = Frontend('paulinha')

    print(f'build: {Employee.count} truckpaders!')

    liang.work()
    parazinho.work()
    paulinha.work()

    review = Service()
    review.work([liang, parazinho, paulinha])








