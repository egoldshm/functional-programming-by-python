import eratosthenes
def twinp(n):
    def _twinp(arr):
        if(len(arr)<2):
            return {}
        if arr[0] + 2 == arr[1]:
            return {**{arr[0]: arr[1]}, **_twinp(arr[1:])}
        return _twinp(arr[1:])
    return _twinp(eratosthenes.napa(n))

def printDictLineByLine(dic):
    if(len(dic.items()) < 1):
        return
    print(str(list(dic.items())[0][0]) + ", " + str(list(dic.items())[0][1]))
    printDictLineByLine(dict(list(dic.items())[1:]))
    
def inputNumAndPrintTwinPrime():
    printDictLineByLine(twinp(int(input("Enter a number for twin prime number:\n>"))))

if __name__ == "__main__":
    inputNumAndPrintTwinPrime()
