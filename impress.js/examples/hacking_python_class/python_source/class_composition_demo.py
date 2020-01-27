import random
class Po:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'PO==>{self.name}: talking issue')
class Dev:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'DEV**>{self.name}: discuss issue')
    def vote(self):
        print(f'DEV-->{self.name}: vote issue: {random.randint(1, 21)}')
class Room:
    def prepare(self):
        print(f'{self.__class__.__name__}:prepare air condition\n{self.__class__.__name__}:prepare tv\n')
class PlanningEvent:
    def __init__(self, room, po, devs):
        self.room, self.po, self.devs = room, po, devs
    def start(self):
        self.room.prepare()
        self.po.talk()
        for dev in self.devs: dev.talk()
        for dev in self.devs: dev.vote()
if __name__ == '__main__':
    event = PlanningEvent(Room(), Po('alice'), [Dev('bob'), Dev('lucy')])
    event.start()
