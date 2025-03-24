# Main class
class Staff:
    def __init__(self, name, DoB, sex, staffID, address):
        self.name = name
        self.DoB = DoB
        self.sex = sex
        self.staffID = staffID
        self.address = address
    
    def setName(self, newName):
        if type(newName) == str:
            self.name = newName
        else:
            raise Exception("Name must be a string")
    
    def setDoB(self, newDoB):
        if type(newDoB) == str:
            self.DoB = newDoB
        else:
            raise Exception("Date of birth must be a string")
    
    def setSex(self, newSex):
        if type(newSex) == str:
            self.sex = newSex
        else:
            raise Exception("Sex must be a string")
    
    def setStaffID(self, newStaffID):
        if type(newStaffID) == int:
            self.staffID = newStaffID
        else:
            raise Exception("StaffID must be a number")
    
    def setAddress(self, newAddress):
        if type(newAddress) == str:
            self.address = newAddress
        else:
            raise Exception("Address must be a string")

    def display(self):
        print(f"Name: {self.name}\nDoB: {self.DoB}\nSex: {self.sex}\nStaffID: {self.staffID}\nAddress: {self.address}")

# Child class of Staff
class Employee(Staff):
    def __init__(self, name, DoB, sex, staffID, address, wage, hireDate):
        super().__init__(name, DoB, sex, staffID, address)
        self.wage = wage
        self.hireDate = hireDate
    
    def setWage(self, newWage):
        if type(newWage) == float:
            self.wage = newWage
        else:
            raise Exception("Wage must be a float")
    
    def setHireDate(self, newHireDate):
        if type(newHireDate) == str:
            self.hireDate = newHireDate
        else:
            raise Exception("Hire Date must be a string")
    
    def display(self):
        super().display()
        print(f"Wage: {self.wage}\nHireDate: {self.hireDate}")

if __name__ == "__main__":
    print("Question A8 & A9\n")
    staff1 = Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
    staff1.display()
    print("\n")

    staff2 = Employee("John", "11/03/04", "male", 2, "1 Waterwheel ville", 25000.0, "23/05/23")
    staff2.display()

    print("\n\nQuestion A10\n")

    staff1.setAddress("34 millenium rd")
    staff1.setName("Bob")
    staff1.display()
    print("\n")

    staff2.setWage(37000.0)
    staff2.setName("Johnson")
    staff2.display()