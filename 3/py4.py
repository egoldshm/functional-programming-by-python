def reverseNum1(n):
	return (n/abs(n))*int(str(abs(n))[::-1])
def isPalindrome(n):
        if(len(str(n))<2):
                return True
        if(n%10 == int(str(n)[-1])):
                return True and isPalindrome(int(str(n)[1:-1]))
        return False


def inputNumAndPrintIfIsPalindrome():
    if(isPalindrome(int(input("Enter a number:\n>")))):
        print("It is a palindrome!!!")
    else:
        print("It is not a palindrome")
if __name__ == "__main__":
    inputNumAndPrintIfIsPalindrome()
