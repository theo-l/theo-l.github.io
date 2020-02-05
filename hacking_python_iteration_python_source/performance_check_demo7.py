import time
repeats, repeat_list = 5000, range(5000)

def timer(func, *args, **kwargs):
    start = time.clock()
    for i in repeat_list: result = func(*args, **kwargs)
    return (time.clock() - start, result)

def for_loop():
    res = []
    for x in repeat_list: res.append(abs(x))
    return res

def list_comprehension():
    return [abs(x) for x in repeat_list]

def map_call():
    return list(map(abs, repeat_list))

def generator_expression():
    return list((abs(x) for x in repeat_list))

def gen_function():
    def gen():
        for x in repeat_list: yield abs(x)
    return list(gen())

if __name__ == "__main__":
    for test in (for_loop, generator_expression, gen_function, list_comprehension, map_call):
        elapsed, result = timer(test)
        print('-' * 33, '\n\n<%-9s>: %.5f => [%s...%s]' % (test.__name__.upper(), elapsed, result[0], result[-1]))
