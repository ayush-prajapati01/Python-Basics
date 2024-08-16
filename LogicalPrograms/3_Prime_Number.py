'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to check whether the number is Prime number

'''


import math


def check_prime_number(num):
    """

    Description: 
        This function used to check whether Prime Number or not
    Parameters:
        n: It specfies the number to be checked
    Return:
        boolean: Whether prime number

    """
    flag = True
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            flag = False
            break
    
    return flag


def main():
    num = input("Enter the number: ")
    if num.isdigit():
        if check_prime_number(int(num)):
            print(f"The {num} is Prime number")
        else:
            print(f"The {num} is Not Prime number")
    
    else:
        print("Please enter a valid number")


if __name__ == "__main__":
   main()