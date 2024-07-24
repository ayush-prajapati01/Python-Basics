'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Swap two numbers

'''


def swap(num1,num2):
    """

    Description: 
        This function used to swap two numbers
    Parameters:
        num1, num2: The numbers to be swapped
    Return:
        int: swapped numbers

    """
    temp = num1
    num1 = num2
    num2 = temp

    return num1, num2


def main():
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    print("\nNumbers before swapping:")
    print("First number:", first_number)
    print("Second number:", second_number)

    first_number, second_number = swap(first_number, second_number)

    print("\nNumbers After swapping:")
    print("First number:", first_number)
    print("Second number:", second_number)


if __name__ == "__main__":
    main()