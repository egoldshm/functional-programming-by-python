def onlyTupleToList(arr):
    newList = []
    for item in arr:
        if isinstance(item, tuple):
            for i in item:
                newList.append(i)

    return newList

def onlyListToTuple(arr):
    newTuple = ()
    for item in arr:
        if(isinstance(item,list)):
            for i in item:
                newTuple = newTuple + (i,)
    return newTuple

def onlyStringToList(arr):
    newList = []
    for item in arr:
        if isinstance(item, str):
            newList.append(item)

    return newList

def onlyNumberToList(arr):
    newList = ()
    list1 = onlyListToTuple(arr)
    list2 = onlyTupleToList(arr)
    for item in arr:
        if isinstance(item, (int, float, complex)):
            for i in list(list1) + list2:
                if i == item:
                    break
            else:
                newList = newList + (item, )

    return newList

def main(arr):
    print(onlyTupleToList(arr))
    print(onlyListToTuple(arr))
    print(onlyStringToList(arr))
    print(onlyNumberToList(arr))
