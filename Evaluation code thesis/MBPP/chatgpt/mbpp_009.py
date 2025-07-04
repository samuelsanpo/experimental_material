#Write a function larg_nnum to get the n largest items from a dataset.
def larg_nnum(dataset, n):
    return sorted(dataset, reverse=True)[:n]
