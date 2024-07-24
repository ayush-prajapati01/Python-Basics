'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Compute Quotient and Remainder

'''


def calc_quotient_remainder(dividend, divisor):
    """

    Description: 
        This function used to calculate Quotient and Remainder
    Parameters:
        dividend: The dividend for divison
        divisor: The divisor for divison
    Return:
        int: quotient
        float: remainder

    """
    return dividend // divisor, dividend % divisor


def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    quotient, remainder = calc_quotient_remainder(dividend,divisor)
    print("Quotient:", quotient)
    print("Remainder:", remainder)


if __name__ == "__main__":
    main()