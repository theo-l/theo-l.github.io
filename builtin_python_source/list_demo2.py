def list_demo():

    ##################################################
    demo_list = [1, 'a', [2, 3, 4], {5, 6, 7}, {'name': 'dave', 'age': 30}]

    # access/assign list element's value by index
    print(f'access list element before assign, demo_list[0] = ', demo_list[0])
    demo_list[0] = 100
    print(f'access list element after assign, demo_list[0] = ', demo_list[0])

    # get the position of element in list
    print(f"Index of 'a' =", demo_list.index('a'))

    # count the number of given value in list
    print(demo_list.count(100))
    demo_list.append(100)
    print(demo_list.count(100))

    # extend a list with another list
    # demo_list.

    # insert an element into a list by the given index position
    demo_list.insert(1, 'bb')
    print(demo_list)

    poped_value = demo_list.pop()  # popup the last element from list
    print(poped_value, demo_list)
    poped_value = demo_list.pop(1) # popup the element from list by index 
    print(poped_value, demo_list)



    # clean all element from the list
    demo_list.clear()
    print(f'after clean all element in the list demo_list = ', demo_list)


if __name__ == "__main__":
    list_demo()
