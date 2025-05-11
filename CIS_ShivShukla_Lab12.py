"""Shiv Shukla
Griwzow
CIS 129
Module 12 Lab"""

# Pet Information Lab

class Pet: # create Pet class
    def __init__(self, name = "", petType = "", age = 0): # initialize fields within class
        self.__name = name # assign private object self.__name to name (and the same for type and age below)
        self.__type = petType
        self.__age = int(age) # converts age field to an integer when stored in age object

    def setName(self, name): # define method setter to change name object
        self.__name = name
    
    def setType(self, petType): # define method setter to change type object
        self.__type = petType
    
    def setAge(self, age): # define method setter to change age object
        self.__age = age

    def getName(self): # define method getter to view name object
        return self.__name

    def getType(self): # define method getter to view type object
        return self.__type

    def getAge(self): # define method getter to view age object
        return self.__age

def main(): # defines main function
    inputName = "" # initializes input-storing objects
    inputType = ""
    inputAge = ""
    Animal = "" # initializes Animal object
    
    Animal = Pet() # assigns Animal as an object under the Pet class (becomes self)
    
    inputName = input("Enter your pet's name: \n") # request name (and type and age inputs below)
    Animal.setName(inputName) # set Animal's name (and type and age fields below) to input-storing object
    inputType = input("Enter your pet's type: \n")
    Animal.setType(inputType)
    inputAge = input("Enter your pet's age: \n")
    Animal.setAge(inputAge)
    
    print("The pet name is:", Animal.getName()) # display Animal's name (and type and age fields below)
    print("The pet type is:", Animal.getType())
    print("The pet age is:", Animal.getAge())

if __name__ == "__main__": # calls main function if script runs main() directly (as opposed to imported)
    main()

