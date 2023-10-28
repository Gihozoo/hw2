import unittest
from salary import Salary  # Import the Salary class from your module


class TestSalary(unittest.TestCase):
    def test_calculate_monthly_salary(self):
        # Test the calculate_monthly_salary method
        salary1 = Salary(employee_id=1, base_salary=5000, allowances=1000, bonuses=200, deductions=500)
        result = salary1.calculate_monthly_salary()

        self.assertEqual(result['Base Salary'], 5000)
        self.assertEqual(result['Allowances'], 1000)
        self.assertEqual(result['Bonuses'], 200)
        self.assertEqual(result['Deductions'], 500)
        self.assertEqual(result['Tax Amount'], 940)  # 0.2 * (5000 + 200 - 500) = 900
        self.assertEqual(result['Net Pay'], 4760)  # 5000 + 1000 + 200 - 900 - 500 = 4800

    def test_display_salary(self):
        # Test the display_salary method by capturing the printed output
        salary2 = Salary(employee_id=2, base_salary=6000, allowances=1200, bonuses=300, deductions=600)

        # Redirect stdout to capture the printed output
        import sys
        from io import StringIO
        original_stdout = sys.stdout
        sys.stdout = StringIO()

        salary2.display_salary()

        output = sys.stdout.getvalue()
        sys.stdout = original_stdout

        expected_output = "Salary details for Employee 2:\nBase Salary: 6000.00\nAllowances: 1200.00\nBonuses: 300.00\nDeductions: 600.00\nTax Amount: 1140.00\nNet Pay: 5760.00\n"
        self.assertEqual(output, expected_output)


if __name__ == '__main__':
    unittest.main()
