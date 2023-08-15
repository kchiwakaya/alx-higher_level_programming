#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first two elements of two tuples together
    and returns the result
    """
    tuple_c = ()
    for i in range(0,2):
        if i >= len(tuple_a):
            holder1 = 0
        else:
            holder1 = tuple_a[i]
        if i >= len(tuple_b):
            holder2 = 0
        else:
            holder2 = tuple_b[i]

        if (i == 0):
            tuple_c = (holder1 + holder2)
        else:
            tuple_c = (tuple_c, holder1 + holder2)

    return (tuple_c)
