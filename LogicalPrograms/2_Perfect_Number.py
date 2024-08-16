'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to check whether the number is Perfect number

'''


def check_perfect_number(num):
    """

    Description: 
        This function used to check whether Perfect Number or not
    Parameters:
        n: It specfies the number to be checked
    Return:
        boolean: Whether perfect number

    """
    divisor_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == num:
        return True
    else:
        return False
  

def main():
    num = int(input("Enter a number: "))
    if num > 0:
        if check_perfect_number(num):
            print(num, "is a perfect number.")
        else:
            print(num, "is not a perfect number.")
    else:
        print("Please enter a positive number.")


if __name__ == "__main__":
   main()


