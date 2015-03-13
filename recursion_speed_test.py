a=list([i for i in range(100)])

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


def lazysum(numList):
    c=0
    for i in numList:
        c+=i 
    return c 

def built_in(numlist):
    return sum(numlist)


print t.timeit('listsum(a)', 'from __main__ import listsum,a', number=1000)
print t.timeit('lazysum(a)', 'from __main__ import lazysum,a', number=1000)
print t.timeit('built_in(a)', 'from __main__ import built_in,a', number=1000)
