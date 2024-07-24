'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Find the Largest Among Three Numbers

'''


def max_of_three_numbers(n1, n2, n3):
    """

    Description: 
        This function used to calculate maximum of three numbers
    Parameters:
        n1,n2,n3: The numbers to be checked
    Return:
        int: maximum number

    """
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    print(f"The maximum of {num1}, {num2}, and {num3} is 
          {max_of_three_numbers(num1,num2,num3)}")


if __name__ == "__main__":
    main()