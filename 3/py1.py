def pentaNumRange1(n1,n2):
        if(n1=>n2):
                return 0
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return pentaNumRange1(n1 + 1, n2) + getPentaNum(n1)
def pentaNumRange2(n1,n2, num):
        if(n1 => n2):
                return num
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return pentaNumRange1(n1 + 1, n2,num + getPentaNum(n1))

def PrintArr10inList_noLoop(arr):
        def printLine(arr, line):
                return "\t".join(map(lambda num: str(num), arr[10*line: len(arr) if  10*line + 10 > len(arr) else 10*line + 10]))
        print("\n".join(map(lambda line: printLine(arr, line), range(int(round(len(arr)/10))))))


def inputNumsAndPrintPentaNum():
        pentaNumArr = pentaNumRange(int(input("Enter a first num for the range of:\n>")),
                                int(input("Enter a second num for the range of:\n>")))
        PrintArr10inList_byLoop(pentaNumArr)
        print()
        PrintArr10inList_noLoop(pentaNumArr)

if __name__ == "__main__":
        inputNumsAndPrintPentaNum()
