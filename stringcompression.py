def stringcompression(str1):

    finalstr = []
    countunique = 0
    freq = []
    uniqalp = []
    for i in range(0,len(str1)):
        if (i==0):
            finalstr.append(str1[i])
            finalstr.append(str(str1.count(str1[i])))

        elif not (str1[i] in finalstr):
            finalstr.append(str1[i])
            finalstr.append(str(str1.count(str1[i])))


    return ''.join(finalstr)

print stringcompression('aaabbcccc')