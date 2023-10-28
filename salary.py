class Salary:
    tax_rate = 0.2  # Example tax rate (20%)

    def __init__(self, employee_id, base_salary, allowances=0, bonuses=0, deductions=0, ):
        self.employee_id = employee_id
        self.base_salary = float(base_salary)
        self.allowances = float(allowances)
        self.bonuses = float(bonuses)
        self.deductions = float(deductions)

    def calculate_monthly_salary(self):
        taxable_income = self.base_salary + self.bonuses - self.deductions
        tax_amount = taxable_income * self.tax_rate
        net_pay = self.base_salary + self.allowances + self.bonuses - tax_amount - self.deductions

        return {
            "Base Salary": self.base_salary,
            "Allowances": self.allowances,
            "Bonuses": self.bonuses,
            "Deductions": self.deductions,
            "Tax Amount": tax_amount,
            "Net Pay": net_pay,
        }

    def display_salary(self):
        salary_details = self.calculate_monthly_salary()
        print(f"Salary details for Employee {self.employee_id}:")
        for component, amount in salary_details.items():
            print(f"{component}: {amount:.2f}")


# # Example usage:
#
# # Create instances of the Salary class for two employees
# employee1 = Salary(1, 60000, allowances=2000, bonuses=3000, deductions=5000)
# employee2 = Salary(2, 75000, allowances=2500, deductions=6000)
#
# # Display the calculated salary for each employee
# employee1.display_salary()
# print("\n")
# employee2.display_salary()
