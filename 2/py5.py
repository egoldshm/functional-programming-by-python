def m(n):
    return sum(map(lambda i: i/(i+1), range(1,n +1)))

def inputNumAndPrintM():
    print("\n".join(map(lambda i: str(i) + "     :" + str(m(i)),
                        range(1,int(input("Enter a number:\n>")) +1 ))))

if __name__ == "__main__":
    inputNumAndPrintM()
