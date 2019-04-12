def Merge3(dict1, dict2,dict3): 
    res = {**dict1, **dict2, **dict3} 
    return res 

def Merge2(dict1, dict2): 
    res = {**dict1, **dict2} 
    return res 


def add3dicts(d1,d2,d3):
    return Merge2(itemsThatInAll(d1,d2,d3),notInAll(d1,d2,d3))
    

def itemsThatInAll(d1,d2,d3):
    list1 = list(filter(lambda item: item in d2 and item in d3,d1))
    return dict(zip(list1,list(map(lambda item: (d1[item],d2[item],d3[item]),list1))))

def notInAll(d1,d2,d3):
    list1 = list(filter(lambda item: item not in itemsThatInAll(d1,d2,d3),d1))
    list2 = list(filter(lambda item: item not in itemsThatInAll(d1,d2,d3),d2))
    list3 = list(filter(lambda item: item not in itemsThatInAll(d1,d2,d3),d3))
    return Merge3(dict(zip(list1, map(lambda i: d1[i], list1))), dict(zip(list2, map(lambda i: d2[i], list2))), dict(zip(list3, map(lambda i: d3[i], list3))))

def input3dictsAndMarge():
    print(add3dicts(eval(input("Enter the first dict:\n>")),eval(input("Enter the second dict:\n>")),eval(input("Enter the 3 dict:\n>"))))

if __name__ == "__main__":
    input3dictsAndMarge()
