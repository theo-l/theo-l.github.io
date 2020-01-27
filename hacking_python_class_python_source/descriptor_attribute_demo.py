class DescriptorAttr:
    def __init__(self, value=None):
        print(f'--------Init attribute value:<{value}> in DescriptorAttr.__init__')
        self._value = value

    def __get__(self, instance, klass):
        print(f'--------Before access attribute value:<{self._value}> in DescriptorAttr.__get__')
        print('Access by class' if not instance else 'Access by instance')
        result = self._value
        print(f'--------After access attribute value:<{self._value}> in DescriptorAttr.__get__')
        return result

    def __set__(self, instance, value):
        print(f'--------Before set attribute value:<{value}> in DescriptorAttr.__set__')
        self._value = value
        print(f'--------After set attribute value:<{value}> in DescriptorAttr.__set__')

class Employee:
    name = DescriptorAttr('truckpader')

if __name__ == "__main__":
    truckpader = Employee()
    print(truckpader.name) # access descriptor attribute by instance object
    print(Employee.name) # access descriptor attribute by class object
    truckpader.name = 'alice'

