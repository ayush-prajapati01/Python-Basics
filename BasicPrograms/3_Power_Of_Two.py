'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Calculate and display table of Power of 2

'''


def power_of_two(n):
    """

    Description: 
        This function used to calculate power of 2
    Parameters:
        n: It specfies the number whose power of 2 is to be calculated
    Return:
        int
            2 raise to n

    """
    return 2 ** n


def main():
    n = int(input("Enter the power value N: "))

    if (n >= 0 and n < 31):
        for i in range(0, n+1):
            print(power_of_two(i))
    else:
        print("Please entere between 0 and 31")


if __name__ == "__main__":
    main()