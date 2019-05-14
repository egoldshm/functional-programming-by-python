def sortedzip(L):
    #תבנית MAP. מקרה בסיסי: רשימה ריקה. מקרה כללי: רשימה לא ריקה אז תמיין. רקורסית זנב. לינארי
    def createSortedList(L, result = []):
        if(L == []):
            return result
        return createSortedList(L[1:], result+[sorted(L[0])])
    return zip(*createSortedList(L))

def reversedzip(L):
    #תבנית MAP. מקרה בסיסי: רשימה ריקה. מקרה כללי: רשימה לא ריקה אז תמיין. רקורסית זנב. לינארי
    def createReveserdList(L, result = []):
        if(L == []):
            return result
        return createReveserdList(L[1:], result+[reversed(L[0])])
    return zip(*createReveserdList(L))

def funczip(func,L):
    return func(L)

def unzippy(L):
    def unzippyRec(L, result):
        if(L == []):
            return result
        return unzippyRec(L[1:], result+[list(L[0])])
    return unzippyRec(L, [None]*len(L[0]))
