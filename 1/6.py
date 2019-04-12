def GetDictionaryOfTypes(arr):
    dictionary = {list: 0,
                  int: 0,
                  float: 0,
                  str: 0,
                  tuple:0}
    
    for item in arr:
        dictionary[type(item)] += 1
    return dictionary
            
