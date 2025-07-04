#\ndef is_happy(s):\n    \"\"\"You are given a string s.\n    Your task is to check if the string is happy or not.\n    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct\n    For example:\n    is_happy(a) => False\n    is_happy(aa) => False\n    is_happy(abcd) => True\n    is_happy(aabb) => False\n    is_happy(adb) => True\n    is_happy(xyy) => False\n    \"\"\"\n
def is_happy(s):
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if len({s[i], s[i+1], s[i+2]}) < 3:
            return False
    return True
