import unittest
from datetime import datetime

class Attendance:
    attendance_records = {}

    def __init__(self, employee_id, date, in_time, out_time):
        self.employee_id = employee_id
        self.date = date
        self.in_time = in_time
        self.out_time = out_time

    @classmethod
    def record_attendance(cls, employee_id, date, in_time, out_time, hrmis):
        if employee_id not in hrmis.employees:
            print(f"Employee with ID {employee_id} does not exist. Cannot record attendance.")
            return

        attendance_record = cls(employee_id, date, in_time, out_time)
        cls.attendance_records.setdefault(employee_id, []).append(attendance_record)

    @classmethod
    def display_records(cls, emp_id=None):
        if emp_id:
            return cls.attendance_records.get(emp_id, [])
        return cls.attendance_records

    @classmethod
    def display_all_records(cls):
        all_records = {}
        for emp_id, records in cls.attendance_records.items():
            all_records[emp_id] = [str(record) for record in records]
        return all_records

    @classmethod
    def calculate_total_hours(cls, emp_id, start_date, end_date):
        records = cls.display_records(emp_id)
        total_hours = 0

        for record in records:
            record_date = datetime.strptime(record.date, "%Y-%m-%d")
            if start_date <= record_date <= end_date:
                in_time = datetime.strptime(record.in_time, "%I:%M %p")
                out_time = datetime.strptime(record.out_time, "%I:%M %p")
                working_hours = (out_time - in_time).total_seconds() / 3600
                total_hours += working_hours

        return total_hours

    def __str__(self):
        return f"Employee ID: {self.employee_id}, Date: {self.date}, In Time: {self.in_time}, Out Time: {self.out_time}"

class TestAttendance(unittest.TestCase):
    def setUp(self):
        # Define sample attendance records for testing
        self.attendance1 = Attendance(1, "2023-10-01", "09:00 AM", "05:00 PM")
        self.attendance2 = Attendance(2, "2023-10-01", "08:30 AM", "04:30 PM")
        self.attendance3 = Attendance(1, "2023-10-02", "09:15 AM", "05:15 PM")

    def test_record_attendance(self):
        # Test the record_attendance method
        hrmis = MockHRMIS()
        Attendance.record_attendance(1, "2023-10-01", "09:00 AM", "05:00 PM", hrmis)

        records = Attendance.display_records(1)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].employee_id, self.attendance1.employee_id)
        self.assertEqual(records[0].date, self.attendance1.date)
        self.assertEqual(records[0].in_time, self.attendance1.in_time)
        self.assertEqual(records[0].out_time, self.attendance1.out_time)

    def test_display_records(self):
        # Test the display_records method
        hrmis = MockHRMIS()
        Attendance.record_attendance(1, "2023-10-01", "09:00 AM", "05:00 PM", hrmis)

        records = Attendance.display_records(1)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].employee_id, self.attendance1.employee_id)
        self.assertEqual(records[0].date, self.attendance1.date)
        self.assertEqual(records[0].in_time, self.attendance1.in_time)
        self.assertEqual(records[0].out_time, self.attendance1.out_time)

        all_records = Attendance.display_all_records()
        self.assertEqual(len(all_records), 1)
        self.assertEqual(len(all_records[1]), 1)
        self.assertEqual(all_records[1][0], str(self.attendance1))

    def test_calculate_total_hours(self):
        # Test the calculate_total_hours method
        hrmis = MockHRMIS()
        Attendance.record_attendance(1, "2023-10-01", "09:00 AM", "05:00 PM", hrmis)
        Attendance.record_attendance(1, "2023-10-02", "09:15 AM", "05:15 PM", hrmis)

        start_date = datetime.strptime("2023-10-01", "%Y-%m-%d")
        end_date = datetime.strptime("2023-10-02", "%Y-%m-%d")

        total_hours = Attendance.calculate_total_hours(1, start_date, end_date)
        self.assertEqual(total_hours, 16.0)  # 8 hours on both days

class MockHRMIS:
    # Define a mock HRMIS class to be used in tests
    employees = [1, 2, 3]  # Sample employee IDs

if __name__ == '__main__':
    unittest.main()
