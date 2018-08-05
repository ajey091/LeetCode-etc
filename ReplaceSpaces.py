def ReplaceSpaces(str):
    i = len(str)-1
    while (i>=0) and (str[i]== ' '):
        str = str[:-1]
        i = i - 1

    newstr = ''
    for i in range(0,len(str)):
        if (str[i] == ' '):
            newstr = newstr + '%20'
        else:
            newstr = newstr + str[i]

    return newstr

print ReplaceSpaces('i am a boy   ')