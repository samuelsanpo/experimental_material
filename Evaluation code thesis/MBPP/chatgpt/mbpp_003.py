#Write a function specified_element to extract every specified element from a given two dimensional list.
def specified_element(matrix, index):
    return [row[index] for row in matrix if len(row) > index]
