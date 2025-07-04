#Write a function group_keyvalue to group a sequence of key-value pairs into a dictionary of lists.
from collections import defaultdict

def group_keyvalue(pairs):
    d = defaultdict(list)
    for k, v in pairs:
        d[k].append(v)
    return dict(d)
