# Import the 'Employee' class from the 'employee' module
from employee import Employee


# Define a child class called 'Manager' that inherits from the 'Employee' class
class Manager(Employee):
    # Constructor method to initialize a Manager object
    def __init__(self, first_name, last_name, salary,  department,benefits, direct_report, rate):
        # Call the constructor of the parent class 'Employee' using super()
        super().__init__(first_name, last_name, salary, department)
        self.__department = department
        self.__direct_report = direct_report
        self.__rate = rate

    # Override the calculate_earnings method to calculate manager's earnings
    def calculate_earnings(self):
        # Calculate earnings by adding base salary and a bonus based on the rate
        earnings = self._salary + (self.__rate * self._salary)
        return earnings

    def set_direct_reports(self, num_reports):
        self.__direct_report += num_reports
        return self.__direct_report

    def set_rate(self, rate):
        self.__rate = rate
        return self.__rate

    # Method to display information of the Manager
    def __str__(self):
        manager_details = super().__str__()
        manager_details += f" Direct report: {self.__direct_report} \n"\
                           f" Rate : {self.__rate} \n"
        return manager_details


