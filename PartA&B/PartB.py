import unittest
import PartA

class StaffUnitTests(unittest.TestCase):
    def test_StaffIsInstance(self):
        staff = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        self.assertTrue(isinstance(staff, PartA.Staff), "Object is not an instance of staff")

    def test_EmployeeIsInstance(self):
        employee = PartA.Employee("John", "11/03/04", "male", 2, "1 Waterwheel ville", 25000.0, "23/05/23")
        self.assertIsInstance(employee, PartA.Employee, "Object is not an instance of employee")
    
    def test_StaffNotInstance(self):
        staff = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        self.assertNotIsInstance(staff, PartA.Employee, "Object is an instance of employee")
    
    def test_ObjectsEqual(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff2 = staff1
        
        self.assertEqual(staff1, staff2, "Objects are not equal")
    
    def test_ObjectsUnequal(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff2 = PartA.Staff("Bob", "15/05/06", "male", 1, "23 Stevenstreet")
        self.assertNotEqual(staff1, staff2, "Objects are Equal")
    
    def test_UpdateName(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff1.setName("Bob")
        self.assertEqual(staff1.name, "Bob", "Update method for setname did not work")
    
    def test_UpdateDoB(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff1.setDoB("23/07/24")
        self.assertEqual(staff1.DoB, "23/07/24", "Update method for setDoB did not work")
    
    def test_UpdateSex(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff1.setSex("female")
        self.assertEqual(staff1.sex, "female", "Update method for setSex did not work")
    
    def test_UpdateID(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff1.setStaffID(2)
        self.assertEqual(staff1.staffID, 2, "Update method for setStaffID did not work")
    
    def test_UpdateAddress(self):
        staff1 = PartA.Staff("Steven", "15/05/06", "male", 1, "23 Stevenstreet")
        staff1.setAddress("31 Bobville")
        self.assertEqual(staff1.address, "31 Bobville", "Update method for setAddress did not work")

def main():
    unittest.main()

if __name__ == "__main__":
    main()