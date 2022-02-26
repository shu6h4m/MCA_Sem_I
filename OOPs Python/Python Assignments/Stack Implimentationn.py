
'''
Create a class Vector to represent a 3-dimensional vector having following features:
1. Using operator overloading, define
a) subtraction and
b) multiplication operation
2. Override function str for printing 3d vector.
3. A counter to maintain the total objects of class Vector and a method to retrieve its value.
4. Methods to retrieve the components of a vector.

NOTE: Maintain data hiding feature of OOP; avoid using inbuilt functions.
''' 
from math import sqrt 
  

class Vector: # Definition of Vector class 
  
    
    def __init__(self, x, y, z): # Initialize 3D Coordinates of the Vector 
        self.x = x 
        self.y = y 
        self.z = z 

    
    def __sub__(self, V): #Method to subtract 2 Vectors 
        return Vector(self.x - V.x, self.y - V.y, self.z - V.z) 
  
    
    def __dot__(self, V): #Method to calculate the dot product of two Vectors 
        
          return self.x * V.x + self.y * V.y + self.z * V.z 
  
    
    def __mul__(self, V): #Method to calculate the cross product of 2 Vectors
        
        return Vector(self.y * V.z - self.z * V.y, 
                      self.z * V.x - self.x * V.z, 
                      self.x * V.y - self.y * V.x) 
  
   
    def __repr__(self):  #Method to define the representation of the Vector 
         
        out = str(self.x) + "i "
  
        if self.y >= 0: 
            out += "+ "
        out += str(self.y) + "j "
        if self.z >= 0: 
            out += "+ "
        out += str(self.z) + "k"
  
        return out 
  
  
if __name__ == "__main__": 
  
    vec1 = Vector(1, 2, 2) 
    vec2 = Vector(3, 1, 2) 
    
    print("Subtraction of Vectors : " + str(vec1 - vec2))  # Subtraction of two vectors 
    
    print("Dot Product :  " + str(vec1 ^ vec2)) # Dot product of two vectors
  
    print("Cross Product :  " + str(vec1 * vec2))  # Cross product of two vectors 
    
    print("String represenation of vector1: " + str(vec1)) #String representation of vector
