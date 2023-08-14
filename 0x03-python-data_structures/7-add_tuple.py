#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    adds the first two elements of two tuples together
    and returns the result
    """
    tuplec = ()
    lena = len(tuple_a)
    lenb = len(tuple_b)
    
    for i in range(2):
        if i >= lena:
            holdera = 0
        else:
            holdera = tuple_a[i]
        if i >= lenb:
            holderb = 0
        else:
            holderb = tuple_b[i]

        if (i == 0):
            tuplec = (holdera + holderb)
        else:
            tuplec = (tuplec, holdera + holderb)

    return (tuplec)
