#Write a function intersection_nested_lists to find the nested list elements which are present in another list.
def intersection_nested_lists(nested_list, other_list):
    other_set = set(other_list)
    return [item for sublist in nested_list for item in sublist if item in other_set]
