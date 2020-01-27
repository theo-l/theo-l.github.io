def tracker(obj):
    def tracked_obj(*args, **kwargs):
        print(f'\n****Starting call <{obj.__name__}>!')
        result = obj(*args, **kwargs)
        print(f'****Finihsed call <{obj.__name__}>!')
        return result
    return tracked_obj

def tracked_function():
    print('"caling tracked function!"')

class TrackedClass:
    def __init__(self):
        print('"calling tracked class"')

if __name__ == "__main__":
    tracked_function() # before track the object
    TrackedClass()

    tracked_function = tracker(tracked_function) # track the object
    TrackedClass.__init__ = tracker(TrackedClass.__init__)

    tracked_function() # after track the object
    TrackedClass()
