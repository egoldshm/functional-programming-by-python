import re
def is_number_regex(s):
    """ Returns True is string is a number. """
    if re.match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True
def opion1(arr):
    arr.sort()
    arr.remove(arr[0])
    arr.remove(arr[len(arr) - 1])
    print(arr)
def Main():
    arr = []
    for i in range(1,5):
        while True:
            num = str(input("Enter number "+ str(i) + "\n"))
            if(is_number_regex(num) == True):
                arr.append(num)
                break
            else:
                print("valid number, try again.")
    opion1(arr)
    
Main()
