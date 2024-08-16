'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 24-07-2024 
    @Title : Python program to conver decimal into binary
    
'''


class BinaryConversion:
    """
    Description:
        This function converts Decimal into Binary
    Parameters:
        num: The number to be converted
    Return:
        int: Binary Number
    """
    @staticmethod
    def toBinary(num):
        binary_num = ""
        while(num != 0):
            remainder = num % 2
            binary_num = str(remainder) + binary_num
            num = num // 2
        
        return binary_num


def main():
    number = int(input("Enter the number: "))
    print(f"{BinaryConversion.toBinary(number)}")


if __name__ == "__main__":
    main()
