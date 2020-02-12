def set_demo():

    sa, sb = {1, 2, 2, 3, 4, 5}, {4, 5, 6, 7, 8, 9, 9}
    print({*sa, *sb})
    sa.add(10)
    print(sa)
    print('a intersection b:', sa.intersection(sb), sa & sb)  # and operation on set
    print('a union b:', sa.union(sb), sa | sb)  # or operation on set
    print('a difference b:', sa.difference(sb), sa - sb, )
    print('b difference a:', sb.difference(sa), sb - sa)
    print('a symmetric_difference b:', sa.symmetric_difference(sb), sa ^ sb)
    sa2 = {o for o in sa}  # make a copy of sa
    sa2.update(sb)
    print('set update:', sa2)
    print(sa2.issuperset(sb), sb.issubset(sa2))
    sa3 = {o for o in sa}
    sa3.symmetric_difference_update(sb)
    print('symmetric_difference_update:', sa3)
    sa4 = {o for o in sa}
    sa4.intersection_update(sb)
    print('intersection update:', sa4)
    sa.discard(5)
    print('after discard:', sa)
    sa.remove(2)
    print('after remove:', sa)

    a, *b, c = sa
    print(a, b, c) # unpack set

    a, *b = sa
    print(a, b)
    a, *b, c, d = sa
    print(a, b, c, d)

if __name__ == "__main__":
    set_demo()
