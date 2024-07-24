'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024 
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 24-07-2024 
    @Title : Python program to find the day of the week

'''


class Date:
    @staticmethod
    def dayOfWeek(m, d, y):
        """
        Description:
            This function calculates the day of the week for a given date.
        Parameters:
            m: Month
            d: Day of the month
            y: Year
        Return:
            int: Day of the week (0 for Sunday, 1 for Monday, etc.)
        """
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7
        return d0
    

def main():
    m = int(input("Enter month (1-12): "))
    d = int(input("Enter day (1-31): "))
    y = int(input("Enter year: "))

    if 1 <= m <= 12 and 1 <= d <= 31:
        day = Date.dayOfWeek(m, d, y)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        print(f"The day of the week is: {day} ({days[day]})")
    else:
        print("Please enter valid date values.")


if __name__ == "__main__":
    main()