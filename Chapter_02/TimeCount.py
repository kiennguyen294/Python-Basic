import time


def sumofn(n):
    start = time.time()
    thesum = 0
    for i in range(1, n + 1):
        thesum = thesum + i

    end = time.time()

    return thesum, end - start


print(sumofn(10000000))


def sumofn_02(n):
    start = time.time()
    sum = (n * (n + 1)) / 2
    end = time.time()
    return sum, end - start


print(sumofn_02(10000000))


def anagramSolution(s1,s2):
    stillOK = True
    if len(s1) != len(s2):
        stillOK = False
    alist = list(s2)
    pos1 = 0

    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1

        if found:
            alist[pos2] = None
        else:
            stillOK = False

        pos1 = pos1 + 1
    return  stillOK

print(anagramSolution('abcd', 'dcba'))

def anagramSolution2(s1,s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches

print(anagramSolution2('abcd','dcba'))

def anagram_solution_4(s1,s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

print('This is solution 4')
print(anagram_solution_4('apple','pleap'))