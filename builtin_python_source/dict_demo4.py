def dict_demo():
    da, db = {'name': 'liang'}, {'gender': 'm'}
    print(da, db)
    dc = {**da, **db}  # pack
    print('packed dict:', dc)
    da.update(db)
    print('in place updated dict:', da)
    # da.pop('non_exist') # NOTE: error
    da.pop('non_exist', 'None')  # NOTE: Ok
    da.pop('gender', None)
    da.setdefault('professions', [])
    print(da)
    da['professions'].append('python')
    print(da)
    da.setdefault('professions', [])  # NOTE: no effect
    print(da)
    da.clear()
    print(da)

def ordered_dict_demo():
    from collections import OrderedDict
    da = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2, 'apple': 5}
    print('normal dict:', da)
    value_sorted_dict = OrderedDict(sorted(da.items(), key=lambda o: o[-1]))
    print(value_sorted_dict)
    key_sorted_dict = OrderedDict(sorted(da.items(), key=lambda o: o[0]))
    print(key_sorted_dict)
    print('compare OrderedDict:', value_sorted_dict == key_sorted_dict)
    print('simple dict:', dict(value_sorted_dict) == dict(key_sorted_dict))
    print('{banana} bananas, {apple} apples, {pear} pears, {orange} oranges'.format(**da))

if __name__ == "__main__":
    dict_demo()
    ordered_dict_demo()
