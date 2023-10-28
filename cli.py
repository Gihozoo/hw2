from hrmis import HRMIS
from employee import Employee
from attendance import Attendance
from salary import Salary

def main():
    hrmis = HRMIS()

    while True:
        print("\nHRMIS Command Menu:")
        print("1. Add Employee")
        print("2. Record Attendance")
        print("3. Calculate Salary")
        print("4. Display Employee Records")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            employee_id = int(input("Enter Employee ID: "))
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            salary = float(input("Enter Base Salary: "))
            hrmis.add_employee(employee_id, first_name, last_name, salary)
            print(f"Employee with ID {employee_id} added successfully.")

        elif choice == '2':
            employee_id = int(input("Enter Employee ID: "))
            date = input("Enter Date (YYYY-MM-DD): ")
            in_time = input("Enter In Time (HH:MM AM/PM): ")
            out_time = input("Enter Out Time (HH:MM AM/PM): ")
            hrmis.record_attendance(employee_id, date, in_time, out_time)
            print("Attendance recorded successfully.")

        elif choice == '3':
            employee_id = int(input("Enter Employee ID: "))
            salary_details = hrmis.calculate_salary(employee_id)
            if salary_details:
                print(f"Salary details for Employee {employee_id}:")
                for component, amount in salary_details.items():
                    print(f"{component}: {amount:.2f}")
            else:
                print(f"Employee with ID {employee_id} does not exist in the HRMIS system.")

        elif choice == '4':
            hrmis.display_employee_records()

        elif choice == '5':
            print("Exiting HRMIS.")
            break

        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
