import unittest
from employee import Employee
from attendance import Attendance
from salary import Salary
from hrmis import HRMIS

class TestHRMIS(unittest.TestCase):
    def setUp(self):
        self.hrmis = HRMIS()

    def test_add_employee(self):
        self.hrmis.add_employee(1, "John", "Doe", 60000)
        self.assertTrue(1 in self.hrmis.employees)

    def test_record_attendance(self):
        self.hrmis.add_employee(1, "John", "Doe", 60000)
        self.hrmis.record_attendance(1, "2023-10-28", "09:00 AM", "05:00 PM", self.hrmis)
        records = self.hrmis.attendance.display_records(1)
        self.assertEqual(len(records), 2)

    def test_calculate_salary(self):
        self.hrmis.add_employee(1, "John", "Doe", 60000)
        salary = self.hrmis.calculate_salary(1)
        self.assertIsNotNone(salary)

    def test_display_employee_records(self):
        self.hrmis.add_employee(1, "John", "Doe", 60000)
        self.hrmis.record_attendance(1, "2023-10-28", "09:00 AM", "05:00 PM", self.hrmis)
        output = self.hrmis.display_employee_records()
        self.assertEqual(output, None)

if __name__ == '__main__':
    unittest.main()
