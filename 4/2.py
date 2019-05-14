#תבנית לכל. מקרה בסיסי - מחרוזת ריקה והתו הנוכחי הוא לא אות. מקרה כללי - התו הנוכחי הוא אות. רקורסיה זנבית. לינארית.
def onlyLetterInString(word):
    if(word in (None, "", [])):
        return True
    if(word[0] in "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"):
        return onlyLetterInString(word[1:])
    return False

#תבנית לכל. מקרה בסיסי - רשימה ריקה או המילה הנוכחית שגויה. מקרה כללי - המילה תקינה. רקורסיה זנבית. לינארית.
def onlyLettersInArr(arr):
    if(arr in (None, "", [])):
        return True 
    if(onlyLetterInString(arr[0])):
        return onlyLettersInArr(arr[1:])
    return False

def createTupleForWord(word):
    return list(filter(lambda l: l in "AaEeIiOoUu", word)), list(filter(lambda l: l not in "AaEeIiOoUu" and l in "AaBbCcDdEeFfGgHhIiJjKkLlMm", word)),\
list(filter(lambda l: l not in "AaEeIiOoUu" and l in "NnOoPpQqRrSsTtUuVvWwXxYyZz", word))

#תבנית MAP. מקרה בסיסי - רשימה ריקה. מקרה כללי - עוד לא הגענו לסוף. רקורסיה זנבית. לינארית.
def createListForWords(arr, result = []):
    if(arr == []):
        return result
    return createListForWords(arr[1:], result + [createTupleForWord(arr[0])])

def treatline(lineNr, line):
    if(onlyLettersInArr(line.split()) == False):
        return -1
    return lineNr, dict(zip(line.split(),createListForWords(line.split())))

#תבנית MAP. מקרה בסיסי - רשימה ריקה. מקרה כללי - עוד לא הגענו לסוף. רקורסיה זנבית. לינארית.
def treatLineInFile(arr, result = ()):
    if(arr in (None, "", [])):
        return result
    return treatLineInFile(arr[1:], result + treatline(0, arr[0]))


#היה כתוב שמותר לשהשתמש בלולאה 
def treatxtfile(flname):
    lst = []
    f = open(flname)
    content = f.readlines()
    for i in range(len(content)):
        if(treatline(i,content[i]) != -1):
            lst.append(treatline(i,content[i]))
    f.close()         
    return dict(lst)

def deleteFirst(d):
    return dict(list(fldict.items())[1:])

def findSums(d, sums =(0,0,0)):
    if(len(d) == 0):
        return sums
    el = list(d.items())[0][1]
    return findSums(deleteFirst(d),(sums[0] + len(el[0]),sums[1] + len(el[1]),sums[2] + len(el[2])))

#תבנית REDUCE. מקרה בסיסי - רשימה ריקה. מקרה כללי - עוד לא הגענו לסוף. רקורסיה זנבית. לינארית.
def sikumofayim(fldict, result = {}):
    if(list(fldict.items()) == []):
        return result
    return sikumofayim(deleteFirst(fldict),{len(result): findSums(list(fldict.items())[0][1]), **result})
#function that delete the first element from dicterey
def deleteFirst(d):
    return dict(list(d.items())[1:])

#function that delete the last element from dicterey
def deleteLast(d):
    return dict(list(d.items())[:-1])

#תבנית REDUCE. מקרה בסיסי - מילון ריק. מקרה כללי - מילון לא נריק אז נמחק את האיבר הראשון ונגדיל את הסום. רקורסיה זנבית לינארית.
def findSums(d, sums =(0,0,0)):
    if(len(d) == 0):
        return sums
    el = list(d.items())[0][1]
    return findSums(deleteFirst(d),(sums[0] + len(el[0]),sums[1] + len(el[1]),sums[2] + len(el[2])))

#תבנית REDUCE. מקרה בסיסי - מילון ריק. מקרה כללי - מילון לא נריק אז נמחק את האיבר הראשון ונגדיל את הסום. רקורסיה זנבית לינארית.
def printLineByLineDict(d, sums = (0,0,0)):
    if(d == {}):
        return sums
    el = list(d.items())[-1]
    val = list(d.values())
    print(str(list(d.keys())[-1]) + '\t' +  str(val[-1][0])+ '\t' +  str(val[-1][1])+ '\t' +  str(val[-1][2]))
    return printLineByLineDict(deleteLast(d),(sums[0] + el[1][0], sums[1] + el[1][1],sums[2] + el[1][2]))

def main():
    path = input("Enter the name of the file:\n>")
    print("line\tVowel\tB-M\tN-Z")
    d = sikumofayim(treatxtfile(path))
    sums = printLineByLineDict(d)
    print("\tTotal:")
    print(str(len(d) + 1) + "\t" + str(sums[0]) + "\t" + str(sums[1]) + "\t" + str(sums[2]))

if __name__ == "__main__":
    main()
