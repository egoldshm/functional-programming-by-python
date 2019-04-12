try:
    a = float(input("Enter a:"))
    b = float(input("Enter b:"))
    c = float(input("Enter c:"))
    if(a + b > c and a + c > b and b + c > a):
        print("they are correct triangle sides lengths")
    else:
        print("they are in error")
except:
    print("they are in error")
