def CheckPalindrome(str):
    flag = 0
    str = str.lower()
    for i in range(0, len(str)):
        if (str[i] != ' ') and (str.count(str[i]) != 2):
            flag += 1

    if (flag > 1):
        print flag
        return False
    return True

print CheckPalindrome('Tact cao')