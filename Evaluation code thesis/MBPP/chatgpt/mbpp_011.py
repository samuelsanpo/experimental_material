#Write a function position_min to find all index positions of the minimum values in a given list.
def position_min(lst):
    if not lst:
        return []
    min_val = min(lst)
    return [i for i, val in enumerate(lst) if val == min_val]
