def Sequential_Search(dlist, item):

    pos = 0
    found = False
    
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    
    return found, pos

print(Sequential_Search([1,3,5,8,10,23,35],10))

def sequentialSearch(alist, item): 
    pos = 0
    found = False
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    return found
testlist = [1,3,5,8,10,23,35]
print(sequentialSearch(testlist, 10))
