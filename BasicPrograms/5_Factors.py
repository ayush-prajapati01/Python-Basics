'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Compute the prime factorization using brute force.

'''


import math


def prime_factors(num):
    """

    Description: 
        This function used to calculate Prime factors of a number
    Parameters:
        n: It specfies the number whose prime factors is calculated
    Return:
        list: contains prime factors
        
    """
    factors = []
    for divisor in range(2, int(math.sqrt(num))+1):
        while num % divisor == 0:
            factors.append(divisor)
            num = num // divisor

    if num > 1:
      factors.append(num)

    return factors


def main():
    num_entered = input("Enter a number to find the prime factors: ")

    if num_entered.isdigit():
        factors = prime_factors(int(num_entered))
        print(f"Prime factors of {num_entered} are: {factors}")
    else:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()
