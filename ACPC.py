totallist = [int(i) for i in input().split()]
maxtopics = 0
guyslist = []
smarteams = 0
for n in range(0, totallist[0]):
    line = list(str(input()))
    guyslist += [line]
    guyslist = [[int(y) for y in x] for x in guyslist]
for i in range(0, totallist[0]-1):
    for j in range (i+1, totallist[0]):
        knowntopics = 0
        for q in range (0, totallist[1]):
            if (guyslist[i][q]) or (guyslist[j][q]):
                knowntopics += 1
        if knowntopics > maxtopics:
            maxtopics = knowntopics
            smarteams = 1
        elif knowntopics == maxtopics:
            smarteams += 1
print (maxtopics)
print (smarteams)