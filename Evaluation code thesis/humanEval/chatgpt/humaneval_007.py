#\ndef iscube(a):\n    '''\n    Write a function that takes an integer a and returns True \n    if this ingeger is a cube of some integer number.\n    Note: you may assume the input is always valid.\n    Examples:\n    iscube(1) ==> True\n    iscube(2) ==> False\n    iscube(-1) ==> True\n    iscube(64) ==> True\n    iscube(0) ==> True\n    iscube(180) ==> False\n    '''\n
def iscube(a):
    if a < 0:
        root = round(-(-a) ** (1/3))
        return root ** 3 == -a
    else:
        root = round(a ** (1/3))
        return root ** 3 == a
