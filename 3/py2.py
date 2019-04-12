def sumDigits1(n):
        if(n <= 0):
                return 0
        return (int(n%10) + sumDigits1(n/10))

def sumDigits2(n):
        def _sumDigits(n, num = 0):
                if(n <= 0):
                        return num
                return _sumDigits(int(n/10), int(n%10) + num)
        return _sumDigits(n)

def inputNumAndPrintSumDigits():
    def printSumDigits(n):
        print(sumDigits1(n))
        print(sumDigits2(n))
    printSumDigits(eval(input("Enter a number to print sum digits:\n>")))

if __name__ == "__main__":
        inputNumAndPrintSumDigits()
