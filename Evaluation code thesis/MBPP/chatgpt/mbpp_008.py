#Write a function count_odd to find number of odd elements in the given list using lambda function.
def count_odd(lst):
    return len(list(filter(lambda x: x % 2 != 0, lst)))
