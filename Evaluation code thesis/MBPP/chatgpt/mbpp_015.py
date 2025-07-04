#Write a python function frequency_Of_Largest to find the frequency of the largest value in a given array.
def frequency_Of_Largest(arr):
    if not arr:
        return 0
    largest = max(arr)
    return arr.count(largest)
