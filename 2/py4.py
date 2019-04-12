def reverseNum1(n):
	return (n/abs(n))*int(str(abs(n))[::-1])
def isPalindrome(n):
    return n == reverseNum1(n)
def inputNumAndPrintIfIsPalindrome():
    if(isPalindrome(int(input("Enter a number:\n>")))):
        print("It is a palindrome!!!")
    else:
        print("It is not a palindrome")
if __name__ == "__main__":
    inputNumAndPrintIfIsPalindrome()
