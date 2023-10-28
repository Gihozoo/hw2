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

# # Example usage:
#
# # Record attendance for employees
# Attendance.record_attendance(1, "2023-10-28", "09:00 AM", "05:00 PM")
# Attendance.record_attendance(2, "2023-10-28", "08:30 AM", "04:30 PM")
# Attendance.record_attendance(1, "2023-10-29", "09:15 AM", "05:15 PM")
#
# # Display attendance records
# print("Records for Employee 1:")
# for record in Attendance.display_records(1):
#     print(record)
#
# print("\nRecords for Employee 2:")
# for record in Attendance.display_records(2):
#     print(record)
#
# # Calculate total working hours for Employee 1 for a specified time period
# start_date = datetime.strptime("2023-10-28", "%Y-%m-%d")
# end_date = datetime.strptime("2023-10-29", "%Y-%m-%d")
# total_hours = Attendance.calculate_total_hours(1, start_date, end_date)
# print(f"\nTotal working hours for Employee 1 from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}: {total_hours:.2f} hours")