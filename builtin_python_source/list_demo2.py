def list_demo():

    print([1, 2, 3] + [4, 5, 6, 7])
    print([1, 2, 3] * 2)

    ##################################################
    demo_list = [1, 'a', [2, 3, 4], {5, 6, 7}, {'name': 'dave', 'age': 30}]

    # Insert
    demo_list.insert(1, 'bb')
    print(demo_list)
    demo_list.append(100)
    print(demo_list)
    demo_list.extend([9, 8, 7, 6, 5])
    print(demo_list)

    # Update
    demo_list[0] = 'update'
    print(demo_list)

    # Index and Query
    print(demo_list[:], demo_list[1:3], demo_list[::3])
    print(demo_list.index('a'))

    # Remove
    demo_list.remove('a')
    print(demo_list)
    demo_list.pop()
    print(demo_list)
    demo_list.pop(2)
    print(demo_list)

    demo_list.clear()
    print(demo_list)


def deque_demo():
    from collections import deque
    a = deque('hello')
    print(a)

    a.appendleft('A')
    print(a)

    print(a.popleft())

    a.rotate(1)
    print(a)

    a.rotate(-1)
    print(a)


if __name__ == "__main__":
    list_demo()
