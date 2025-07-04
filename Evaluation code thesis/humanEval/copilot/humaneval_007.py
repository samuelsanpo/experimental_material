#\ndef iscube(a):\n    '''\n    Write a function that takes an integer a and returns True \n    if this ingeger is a cube of some integer number.\n    Note: you may assume the input is always valid.\n    Examples:\n    iscube(1) ==> True\n    iscube(2) ==> False\n    iscube(-1) ==> True\n    iscube(64) ==> True\n    iscube(0) ==> True\n    iscube(180) ==> False\n    '''\n
def iscube(a):
    '''
    Write a function that takes an integer a and returns True 
    if this ingeger is a cube of some integer number.
    Note: you may assume the input is always valid.
    Examples:
    iscube(1) ==> True
    iscube(2) ==> False
    iscube(-1) ==> True
    iscube(64) ==> True
    iscube(0) ==> True
    iscube(180) ==> False
    '''
    return round(a ** (1/3)) ** 3 == a