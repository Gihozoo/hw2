from employee import Employee
from attendance import Attendance
from salary import Salary
from datetime import datetime

class HRMIS:
    def __init__(self):
        self.employees = {}  # Dictionary to store employee records
        self.attendance = Attendance
        self.salary = Salary

    def add_employee(self, employee_id, first_name, last_name, salary):
        employee = Employee(employee_id, first_name, last_name, salary)
        self.employees[employee._Employee__employee_id] = employee

    def record_attendance(self, employee_id, date, in_time, out_time,hrmis):
        self.attendance.record_attendance(employee_id, date, in_time, out_time,hrmis)

    def calculate_salary(self, employee_id):
        if employee_id in self.employees:
            employee_data = self.employees[employee_id]
            salary = self.salary(employee_id, employee_data._salary)
            return salary.calculate_monthly_salary()

    def display_employee_records(self):
        for employee_id, employee in self.employees.items():
            print(f"Employee ID: {employee_id}")
            print(employee)
            print("Attendance Records:")
            attendance_records = self.attendance.display_records(employee_id)
            for record in attendance_records:
                print(record)
            print("Salary Details:")
            salary_details = self.calculate_salary(employee_id)
            for component, amount in salary_details.items():
                print(f"{component}: {amount:.2f}")
            print("\n")

# # Example usage:
#
#
# hrmis = HRMIS()
#
# # Add employees
# hrmis.add_employee(1,"Murinda", "Kenny", 60000)
# hrmis.add_employee(2,"Shema Kagabo", "Dorcy", 75000)
# hrmis.add_employee(2,"Mugabo", "Fabrice", 75000)
#
#
# # Record attendance for employees
# hrmis.record_attendance(1, "2023-10-28", "09:00 AM", "05:00 PM", hrmis)
# hrmis.record_attendance(2, "2023-10-28", "08:30 AM", "04:30 PM", hrmis)
# hrmis.record_attendance(3, "2023-10-29", "09:15 AM", "05:15 PM", hrmis)
#
#
# # Display employee records and salary details
# hrmis.display_employee_records()
