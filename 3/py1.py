def pentaNumRange1(n1,n2):
        if(n1 >= n2):
                return 0
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return pentaNumRange1(n1 + 1, n2) + getPentaNum(n1)
    
def pentaNumRange2(n1,n2, num = 0):
        if(n1 >= n2):
                return num
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return pentaNumRange1(n1 + 1, n2,num + getPentaNum(n1))

def PrintArr10inList_noLoop(arr):
    def printLine(arr, num = 1):
        if(arr == []):
            return
        if(num == 10):
            return arr
        print(str(arr[0]),end = ", ")
        printLine(arr[1:],num + 1)
    if(arr == []):
        return
    PrintArr10inList_noLoop(printLine(arr))


def inputNumsAndPrintPentaNum():
        pentaNumArr = pentaNumRange1(int(input("Enter a first num for the range of:\n>")),
                                int(input("Enter a second num for the range of:\n>")))
        PrintArr10inList_noLoop(pentaNumArr)

if __name__ == "__main__":
        inputNumsAndPrintPentaNum()
