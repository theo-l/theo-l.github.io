def tracker(obj):

    def tracked_obj(*args, **kwargs):
        print(f'\n****Starting call <{obj.__name__}>!')
        result = obj(*args, **kwargs)
        print(f'****Finihsed call <{obj.__name__}>!')
        return result
    return tracked_obj

@tracker
def tracked_function():
    print('"calling tracked function!"')

class TrackedClass:
    @tracker
    def __init__(self):
        print('"calling tracked class!"')

if __name__ == "__main__":
    tracked_function() # call the decorated object
    TrackedClass()
