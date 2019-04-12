def pi(n):
    def getListByFarmula(n):
        return list(map(lambda i: ((-1)**(i+1)/(2*i - 1)),range(1,n+1)))
    return 4*sum(getListByFarmula(n))
def inputNumAndPrintPi():
    print("\n".join(map(lambda i: str(i) + ":\t" + str(pi(i)),
                        range(1,int(input("Enter a number:\n>")) +1 ))))

if __name__ == "__main__":
    inputNumAndPrintPi()
