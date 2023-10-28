# Import the 'Employee' class from the 'employee' module
from employee import Employee


# Define a child class called Director that inherits from the 'Employee' class
class Director(Employee):
    # Constructor method to initialize a Director object
    def __init__(self,first_name, last_name, salary, benefits, department, annual_bonus):
        super().__init__(first_name, last_name, salary, benefits)
        self.__department = department
        self.__annual_bonus = annual_bonus

    def set_annual_bonus(self, bonus):
        self.__annual_bonus = bonus
        return self.__annual_bonus

    # Override the calculate_earnings method to calculate director's earnings
    def calculate_earnings(self):
        # Calculate earnings by adding base salary and annual bonus
        earnings = self._salary + self.__annual_bonus
        return earnings

    # Method to display information of the Director
    def __str__(self):
        director_details = super().__str__()
        director_details += f" Department : {self.__department}\n"
        director_details += f" Annual bonus : {self.__annual_bonus}\n"
        return director_details



