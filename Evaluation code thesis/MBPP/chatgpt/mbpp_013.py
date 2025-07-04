#Write a function remove_tuples to remove all the tuples with length k.
def remove_tuples(lst, k):
    return [t for t in lst if not (isinstance(t, tuple) and len(t) == k)]
