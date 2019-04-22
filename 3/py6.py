def pi1(n):
    if(n < 1):
        return 0
    return 4*((-1)**(n+1)/(2*n - 1)) + pi1(n - 1)

def pi2(n, num = 0):
    if(n < 1):
        return num
    return pi2(n - 1, num + 4*((-1)**(n+1)/(2*n - 1)))
def inputNumAndPrintPi():
    def printSinglePi(n):
        if(n<1):
            return
        printSinglePi(n - 1)
        print(str(n) + ":\t" + str(pi2(n)))
    printSinglePi(int(input("Enter a number:\n>")))

if __name__ == "__main__":
    inputNumAndPrintPi()
