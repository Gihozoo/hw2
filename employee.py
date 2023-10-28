# Import the 'random' module to generate random numbers
import random


# Define the 'Employee' class to represent employees
class Employee:

    # Constructor method to initialize an Employee object
    def __init__(self, employee_id, first_name, last_name, salary):
        # generate a random employee id
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        # Create an email address based on first name and last name
        self.__email = self.__first_name + "." + self.__last_name + "@mycompany.com"
        self._salary = salary

    # Method to set the salary of an employee
    def set_salary(self, amount):
        self._salary = amount
        return self._salary

    def set_benefits(self, benefits):
        self.__benefits = benefits
        return self.__benefits

    # Method to calculate and return the earnings of an employee
    def calculate_earnings(self):
        return self._salary

    # Method to display information of the Employee
    def __str__(self):
        return (f" First name : {self.__first_name}\n"
                f" Last name : {self.__last_name}\n"
                f" email : {self.__email}\n"
                f" Salary : {self.calculate_earnings()}\n"
                f" Employee ID : {self.__employee_id}\n")

