from __future__ import print_function, division


def print_hello(name):
    """  Print "Hello world"
    :return:
    """
    print("Hello "+name)


def add_vars(a, b):
    """
    Add two variables
    :param a:
    :param b:
    :return:
    """
    return a + b


def world_cups():
    """
    Return ordered sequence of world cups
    :return:
    """
    return [("Germany", 2006, "Italy"), ("South-Africa", 2010, "Spain"), ("Brazil", 2014, "Germany")]


def add_to_stack(stack, element):
    """
    Add element to a stack
    :param stack:
    :param element:
    :return:
    """
    stack.append(element)
    return stack


def remove_from_stack(stack):
    """
    Remove element from the stack
    :param stack:
    :return:
    """
    stack.pop()
    return stack


def world_cups_by_key(world_cups_list):
    """
    Return world cups in a dictionary with host+year as key
    :param world_cups_list:
    :return:
    """
    world_cups_with_labels = {}
    for w in world_cups_list:
        world_cups_with_labels[w[0]+str(w[1])] = w
    return world_cups_with_labels


def change_string(s):
    """
    Change a strin
    :param s:
    :return:
    """
    s += "changed"
    return s


def change_int(i):
    """
    Change an int
    :param i:
    :return:
    """
    i += 5
    return i


def change_list(l):
    """
    Change a list
    :param l:
    :return:
    """
    l.append("new")
    return l


def change_dict(d):
    """
    Change a dictionary
    :param d:
    :return:
    """
    d["newKey"] = "newValue"
    return d


def a_appended(a, container=[]):
    """
    Append element to container
    :param a:
    :param container:
    :return:
    """
    container.append(a)
    return container


def add_even_numbers_with_for(end_num):
    """
    Add all even numbers up to the given end with for loop
    :param end_num:
    :return:
    """
    sum_of_even = 0

    for n in range(0, end_num+1):
        if n % 2 == 0:
            sum_of_even += n

    return sum_of_even


def add_even_numbers_with_while(end_num):
    """
    Add all even numbers up to the given end with while loop
    :param end_num:
    :return:
    """
    sum_of_even = 0

    n = 0
    while n < end_num + 1:
        if n % 2 == 0:
            sum_of_even += n
        n += 1

    return sum_of_even


def add_even_numbers_elegant(end_num):
    """
    Add all even numbers up to the given end with generator expression
    :param end_num:
    :return:
    """
    return sum(n for n in range(0, end_num+1) if n % 2 == 0)

###########################
# example dict ???
###########################


def loop_two_lists():
    """ Loop over the two lists and print the corresponding elements
    :return:
    """
    squares = [1, 4, 9,  16, 25]
    cubics = [1, 8, 27, 64, 125]

    for i in range(0, len(squares)):
        print(str(squares[i]) + " " + str(cubics[i]))


def is_a_bigger_square_in_the_list(a):
    """
    Returns if  there is a square in the list that is bigger than the given value
    :param a:
    :return:
    """
    squares = [1, 4, 9,  16, 25]
    for x in squares:
        if x > a:
            break
    else:
        raise ValueError("not found")
    return True


def sum_args_and_kwvalues(*args, **kwargs):
    """
    Sum up values of positional and keyword arguments
    :param args:
    :param kwargs:
    :return:
    """
    return sum(args) + sum(kwargs.values())


def apply_to_all_elements(lst, fct):
    """Apply a user function to all elements of a list and return the result
    in a new list.

    :param lst: List containing the elements to apply `fct` to. This list
        is not changed.
    :type lst: list

    :type fct: callable
    :param fct: User function to apply.

    :return: List containing the function results.
    :rtype: list
    """
    return map(fct, lst)