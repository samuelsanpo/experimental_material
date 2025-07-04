#Write a python function find_Sum to find the sum of repeated elements in a given array.
def find_Sum(arr):
    from collections import Counter
    counts = Counter(arr)
    return sum(key * count for key, count in counts.items() if count > 1)
