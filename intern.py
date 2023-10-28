# Import the 'Employee' class from the 'employee' module
from employee import Employee


# Define a child class called 'Intern' that inherits from the 'Employee' class
class Intern(Employee):
    # Constructor method to initialize an Intern object
    def __init__(self, first_name, last_name, salary, benefits, department,university_name, program_name, internship_duration):
        # Call the constructor of the parent class Employee using super()
        super().__init__(first_name, last_name, salary, benefits)
        self.__university_name = university_name
        self.__department = department
        self.__program_name = program_name
        self.__internship_duration = internship_duration

    # Override the calculate_earnings method to calculate intern's earnings
    def calculate_earnings(self):
        # Calculate earnings by multiplying monthly salary by the internship duration (in months)
        earnings = self._salary * (self.__internship_duration/12)
        return earnings

    def set_internship_duration(self, duration):
        self.__internship_duration = duration
        return self.__internship_duration

    # Method to display information of the intern
    def __str__(self):
        intern_details = super().__str__()
        # Append intern details to the employee details from the employee class
        intern_details += f" University Name: {self.__university_name}\n"\
                          f" Program name: {self.__program_name}\n"\
                          f" Internship duration : {self.__internship_duration}\n"\
                          f" Department : {self.__department}\n"
        return intern_details




