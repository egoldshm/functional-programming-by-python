def sumDigits2(n):
	return sum(map(lambda c: int(c), list(str(abs(n)))))

def sumDigits1(n):
        def byDivide(n, digit):
                return (n/pow(10,digit))%10
        return sum(map(lambda i: int(byDivide(n, i)),range(len(str(n)))))

def inputNumAndPrintSumDigits():
    def printSumDigits(n):
        print(sumDigits1(n))
        print(sumDigits2(n))
    printSumDigits(eval(input("Enter a number to print sum digits:\n>")))

if __name__ == "__main__":
        inputNumAndPrintSumDigits()
