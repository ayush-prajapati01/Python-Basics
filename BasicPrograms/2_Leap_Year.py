'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Determine Leap Year

'''


def is_leap_year(year):
    """

    Description: 
        This function used to determine leap year
    Parameters:
        year: It specfies the year value
    Return:
        Boolean
            Whether lear year or not

    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    

def main():
    year_entered = input("Enter a 4 digit year: ")

    # Checking the length of the year and its type
    if len(year_entered) == 4 and year_entered.isdigit():
        leap_year = is_leap_year(int(year_entered))

        if leap_year:
            print(f"The {year_entered} is a Leap Year")
        else:   
            print(f"The {year_entered} is Not a Leap Year")

    else:
        print("Please enter a 4 digit number.")


if __name__ == "__main__":
    main()
