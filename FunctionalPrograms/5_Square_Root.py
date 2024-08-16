'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 24-07-2024 
    @Title : Python program to calculate square root using Newton's Method
    
'''


class MathOperations:
    @staticmethod
    def sqrt(c):
        """
        Description:
            This function computes the square root of a non-negative number using Newton's method.
        Parameters:
            c: Non-negative number to compute the square root of
        Return:
            float: Approximated square root of the input number
        """
        epsilon = 1e-15
        t = c

        while abs(t - c/t) > epsilon * t:
            t = (c/t + t) / 2

        return t


def main():
    c = float(input("Enter a non-negative number to find its square root: "))

    if c < 0:
        print("Please enter a non-negative number.")
    else:
        result = MathOperations.sqrt(c)
        print(f"The square root of {c} is approximately {result:.5f}")


if __name__ == "__main__":
    main()