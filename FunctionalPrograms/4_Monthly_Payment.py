'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 24-07-2024 
    @Title : Python program to display Monthly payment for a loan.
    
'''


class Loan:
    @staticmethod
    def monthlyPayment(P, Y, R):
        """
        Description:
            This function calculates the monthly payment for a loan.
        Parameters:
            P: Principal loan amount
            Y: Number of years
            R: Annual interest rate (in percentage)
        Return:
            float: Monthly payment amount
        """
        n = 12 * Y
        r = R / (12 * 100)

        payment = (P * r * (1 + r)**n) / ((1 + r)**n - 1)
        return payment


def main():
    P = float(input("Enter principal loan amount: "))
    Y = int(input("Enter number of years: "))
    R = float(input("Enter annual interest rate (%): "))

    monthly_payment = Loan.monthlyPayment(P, Y, R)
    print(f"Monthly payment: Rs{monthly_payment:.2f}")


if __name__ == "__main__":
    main()