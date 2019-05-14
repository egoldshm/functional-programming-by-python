from random import choice
peopleNames = ("Iosi", "Ety", "Eitan")
verbs = ("sees", "plays", "sings","brings" )
adjectives = ("tall", "small", "red","large")
adverbs = ("slowly", "tomorrow", "now", "soon", "suddenly","somewhen")
animateObjects = ("flowers", "oranges","geers", )
inanimateObjects = ("a stone", "a chair","computers" )

#רקורסית זנב. תנאי כללי: גדול מ0. תוסיף משפט. תנאי בסיסי: שווה ל0. לינארי.
def crPoem(N, result = ()):
    if(N == 0):
        return result
    return crPoem(N - 1, result +\
                  (choice(peopleNames) + " " + choice(verbs) + " " + choice(adverbs) \
                   + " " + choice(adjectives)+ " " + choice(animateObjects + inanimateObjects),))

def theHumbletPoet(N):
    print("\n".join(crPoem(N)))
                                   
