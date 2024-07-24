'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Reverse the number

'''


def reverse_number(num):
    """

    Description: 
        This function used to reverse the number
    Parameters:
        n: It specfies the number to be reversed
    Return:
        int: reversed number

    """
    reverse_num = 0
    while(num > 0):
        remainder = num % 10
        num //= 10
        reverse_num = (reverse_num * 10) + remainder
    
    return reverse_num


def main():
    number = int(input("Enter number to reverse: "))
    print(f"The reversed number is {reverse_number(number)}")


if __name__ == "__main__":
   main()

