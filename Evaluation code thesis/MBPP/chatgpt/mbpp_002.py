#Write a function count_pairs to count all the distinct pairs having a difference of k in any array.
def count_pairs(arr, k):
    s = set(arr)
    return sum(1 for x in s if x + k in s)
