#Object named GetName, instance of NameTest.
#When the object is first created there is no argument
#Use a setter to set FirstName and  LastName in one string 
#Use a getter to get FirstName, seperate for LastName

class NameTest():
    def __init__(self, FirstName_LastName = " "):
        self.FirstName_LastName = FirstName_LastName

    def SetName(self, FirstName_LastName = " "):
        self.FirstName_LastName = FirstName_LastName

    def GetFirstName(self):
        return (self.FirstName_LastName.split()[0])

    def GetLastName(self):
        return (self.FirstName_LastName.split()[1])

GetName = NameTest()

#Could I have added FirstName_LastName as an argument to GetFirstName??
