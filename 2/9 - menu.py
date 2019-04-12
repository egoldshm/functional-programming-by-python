import py1
import py2
import py3
import py4
import py5
import py6
import py7
import py8

def showMenu():
    Menu = {1: (py1.inputNumsAndPrintPentaNum,"print penta num"),
            2: (py2.inputNumAndPrintSumDigits, "print sum of digits"),
            3: (py3.inputNumAndPrintReverse, "print reverse number"),
            4: (py4.inputNumAndPrintIfIsPalindrome, "check if number is palindrome"),
            5: (py5.inputNumAndPrintM, "print serial number"),
            6: (py6.inputNumAndPrintPi, "print pi serial"),
            7: (py7.inputNumAndPrintTwinPrime,"print twin prime numbers"),
            8: (py8.input3dictsAndMarge, "marge 3 dictantions"),
            0: (exit, "exit")}
    print("\n".join(map(lambda i: str(i) + ":\t" + Menu[i][1],Menu)))
    choise = int(input("Enter your choise:\n>"))
    if(choise in Menu):
        Menu[choise][0]()
    showMenu()
    



if __name__ == "__main__":
    showMenu()
