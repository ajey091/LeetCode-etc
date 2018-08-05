def OneAway(str1,str2):
    if (abs(len(str1)-len(str2))) > 1:
        return False
    flag = 0
    strnew = str1 + str2
    for i in range(0,len(strnew)):
        if (strnew.count(strnew[i]) == 1):
            flag += 1

    if flag > 1:
        return False

    return True

print OneAway('pale','bake')