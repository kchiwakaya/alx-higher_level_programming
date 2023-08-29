#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    quotient = 0
    for i in range(list_length):
        try:
            quotient = (my_list_1[i] / my_list_2[i])
        except TypeError:
            quotient = 0
            print("wrong type")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            my_list_3.append(quotient)
    return my_list_3