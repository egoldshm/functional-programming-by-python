def pentaNumRange1(n1,n2):
        if(n1 >= n2):
                return []
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return [getPentaNum(n1)] + pentaNumRange1(n1 + 1, n2)
    
def pentaNumRange2(n1,n2, num = 0):
        if(n1 >= n2):
                return [num]
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return pentaNumRange1(n1 + 1, n2,getPentaNum(n1) + [num])

def PrintArr10inList_noLoop(arr):
    def printLine(arr, num = 1):
        if(arr in ([],None)):
            return []
        if(num == 10):
            return arr
        print(arr[0], end = ",\t")
        return printLine(arr[1:],num + 1)
    if(arr == []):
        return
    print()
    PrintArr10inList_noLoop(printLine(arr))


def inputNumsAndPrintPentaNum():
        PrintArr10inList_noLoop(pentaNumRange1(int(input("Enter a first num for the range of:\n>")),
                                int(input("Enter a second num for the range of:\n>"))))

if __name__ == "__main__":
        inputNumsAndPrintPentaNum()
