'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Check number is even or odd

'''


def check_even(num):
    """

    Description: 
        This function used to check number is even or not
    Parameters:
        num: The number to be checked
    Return:
        boolean: Whether even

    """
    if num % 2 == 0:
        return True
    else:
        return False


def main():
    num = input("Enter a number: ")
    if num.isdigit():
        if check_even(int(num)):
            print(f"The entered {num} is Even")
        else:
            print(f"The entered {num} is Odd")

    else:
        print("Please enter a valid number.")


if __name__ == "__main__":
    main()