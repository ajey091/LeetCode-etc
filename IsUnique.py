def IsUnique(str):
    for i in range(0,len(str)):
        temp = str[:i] + str[i+1:]
        if (str[i] in temp):
            return False

    return True

print IsUnique("great")