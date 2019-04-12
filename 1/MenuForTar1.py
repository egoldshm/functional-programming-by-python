#
#  Example program for Targil 1
#
import math

def getNumber(str1):
     while True:
          num = float(input(str1))
          if(num != None):
               return num

#
# Area calculation program  
def rectangleArea(w, h):
     return w*h
#
def circleArea(r):
     return math.pi * r**2

#
def sphereArea(r):
     return math.pi * (4/3)* r**3
#
def coneArea(height, radius):
     return (1/3)*math.pi * (radius**2)*height
#
def squarePyramidArea(height, side):
     return (side*side*height)/3
     
#
# printing the menu options
def prtMenu(shapes):
   for i in range(len(shapes)):
      print (i+1, shapes[i])
   return
#
# main program
#
print ("Welcome to the Area calculation program")
print ("---------------------------------------\n")  
# Print out the menu
shapes = ("Rectangle", "Circle","Sphere","Cone","squarePyramid")
while True:
    print ("\nPlease select a shape (press 0 to quit):")
    prtMenu(shapes) 
    # Get the user's choice: 
    shape = input("> ")
    # Calculate the area: 
    if shape == "1":
         height = getNumber("Please enter the height: ")    
         width  = getNumber("Please enter the width: ")
         area = rectangleArea(width, height)
         print ("The area is", area)
         continue
    elif shape == "2":
         radius = getNumber("Please enter the radius: ")
         area   = circleArea(radius)
         print ("The area is", area)
         continue
    elif shape == "3":
         radius = getNumber("Please enter the radius: ")
         area   = sphereArea(radius)
         print ("The area is", area)
         continue
    elif shape == "4":
         height = getNumber("Please enter the height: ")    
         radius  = getNumber("Please enter the radius: ")
         area = coneArea(height, radius)
         print ("The area is", area)
         continue
    elif shape == "5":
          side = getNumber("please enter the side of square: ")
          height = getNumber("Please enter the height: ")    
          area = squarePyramidArea(height, side)
          print ("The area is", area)
          continue

    elif shape == "0":
         print ("Bye!")
         break
    else:     
         print ("Invalid shape")
