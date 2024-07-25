'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 25-07-2024 
    @Title : Python program to Swap Nibbles of a byte
    
'''


def toBinary(num):
    """
    Description:
        This function converts Decimal into Binary
    Parameters:
        num: The number to be converted
    Return:
        int: Binary Number
    """
    binary_num = ""
    while(num != 0):
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num = num // 2
    
    return binary_num


def toDecimal(binary_str):
    """
    Description:
        This function converts Binary into Decimal 
    Parameters:
        num: The number to be converted
    Return:
        int: Decimal Number
    """
    decimal_num = 0
    n= int(len(binary_str))
    for i in range(0,n):
        decimal_num += int(binary_str[i]) * 2**(n-i-1)
        
    return decimal_num


def swap_nibbles(num):
    """
    Description:
        This function swaps nibble of a byte
    Parameters:
        num: The binary number to be swapped
    Return:
        int: Swapped binary Number
    """
    num = num.zfill(8)
    return num[4:] + num[0:4]


def main():
    number = int(input("Enter a decimal number : "))
    binary_number = toBinary(number)
    swapped_binary_number = swap_nibbles(binary_number)
    swaped_decimal_number = toDecimal(swapped_binary_number)
    print(f"The binary representation of {number} is {binary_number}")
    print(f"The swapped binary number is {swapped_binary_number}")
    print(f"The converted New Decimal number is {swaped_decimal_number}")
    

if __name__ == "__main__":
    main()

