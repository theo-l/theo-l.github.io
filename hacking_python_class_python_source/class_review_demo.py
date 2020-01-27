# 1. NOTE: class' parents collection: **(object, )**
# 2. NOTE: class' name **Employee**
class Employee(object):

    # 3. NOTE: class' attributes: **name**, **position**
    name = None
    position = None

    # 4. NOTE: class' builtin method: **__init__**
    def __init__(self, name, position):

        # 5. NOTE: instance's attributes: **name**, **position**
        self.name = name 
        self.position = position

    # 6. NOTE: user defined class method: **work**
    def work(self):
        pass
