def pentaNumRange(n1,n2):
        getPentaNum = lambda n: int((n*(3*n - 1))/2)
        return list(map(getPentaNum,range(n1,n2)))

def PrintArr10inList_byLoop(arr):
        for i in range(0,len(arr),10):
                for j in range(i, i + 10 if len(arr)> i + 10 else len(arr)):
                        print(arr[j], end = "\t")
                #print("\n")

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
