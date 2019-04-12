import eratosthenes
def twinp(n):
    return dict(zip(filter(lambda num: num + 2 in eratosthenes.napa(n) ,eratosthenes.napa(n)),
filter(lambda num: num - 2 in eratosthenes.napa(n) ,eratosthenes.napa(n))))

def printDictLineByLine(dic):
    print('\n'.join(map(lambda num1,num2:str(num1) + ", " + str(num2),list(dic.keys()),list(dic.values()))))

def inputNumAndPrintTwinPrime():
   printDictLineByLine(twinp(int(input("Enter a number for twin prime number:\n>"))))

if __name__ == "__main__":
    inputNumAndPrintTwinPrime()
