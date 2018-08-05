def CheckPermutation(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    if (len1 != len2):
        return False

    for i in range(0,len1):
        if (str1.count(str1[i]) != str2.count(str1[i])):
            return False

    return True

print CheckPermutation('ginger2','ginger')