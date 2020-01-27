from talks.hacking_python_class.class_inheritance_relation import Chef


class TracerWrapper:

    def __init__(self, obj):
        self.wrapped = obj  # this obj object is embedded in a proxy manager class TracerWrapper

    def __getattr__(self, attribute_name):
        if attribute_name == '__len__':
            return super(TracerWrapper, self).__getattr__(attribute_name)
        print(f'====before proxy tracing access of: {attribute_name}')
        result = getattr(self.wrapped, attribute_name)
        print(f'====after proxy tracing access of: {attribute_name}')
        return result


if __name__ == '__main__':
    chef = TracerWrapper(Chef('bob'))
    # Call a method which is not exist in the proxy class TracerWrapper, will actually
    # call the managed object's method
    chef.work()
