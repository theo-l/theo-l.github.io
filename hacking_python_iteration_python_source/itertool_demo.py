from base_demo import Iterable
import itertools

if __name__ == "__main__":
    iter1 = Iterable([1, 2, 3, 4, 5, 6, 7])
    a, b = itertools.tee(iter1)
    print(list(itertools.islice(a, 4)), b)
