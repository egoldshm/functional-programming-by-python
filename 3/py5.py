def m1(n):
    if(n<1):
        return 0
    return n/(n+1)+ m1(n-1)

def m2(n):
    def _m2(n, num = 0):
        if(n<1):
            return num
        return _m2(n - 1, num + n/(n+1))
    return _m2(n)

def printMFunctionUntil(n):
    if(n<1):
        return
    printMFunctionUntil(n - 1)
    print(m2(n))
    

def inputNumAndPrintM():
    print(printMFunctionUntil(int(input("Enter a number:\n>"))))

if __name__ == "__main__":
    inputNumAndPrintM()
