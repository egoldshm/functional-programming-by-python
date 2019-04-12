def reverseNum1(n):
	return int((n/abs(n))*int(str(abs(n))[::-1]))

def reverseNum2(n):
        return int(str("".join(list(reversed(list(str(abs(n))))))))

def inputNumAndPrintReverse():
        num = int(input("Enter number for reverse:\n>"))
        print(reverseNum1(num))
        print(reverseNum2(num))
        
if __name__== "__main__":
        inputNumAndPrintReverse()
