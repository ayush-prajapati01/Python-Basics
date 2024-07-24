'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Simulate Lottery Coupon Numbers

'''


import random


class CouponGenerator:
    """

    Description: 
        This class is used to generate Coupons
    Method:
        generate_coupon_number()

    """
    @staticmethod
    def generate_coupon_number(n):
        """

        Description: 
            This function used to genrate random coupon number
        Parameters:
            n: It specfies the number of coupons to be generated
        Return:
            list: Containg coupon numbers

        """
        lucky_coupon_numbers = []
        for _ in range(n):	
            lucky_coupon_numbers.append(random.randint(1000, 9999))

        return lucky_coupon_numbers


def check_coupon_no(lucky_coupon, coupon):
    """

    Description: 
        This function used to check similarity between 2 coupons
    Parameters:
        lucky_coupon, coupon: coupon numbers to be checked
    Return:
        boolean: Whether same coupon number

    """
    if lucky_coupon == coupon:
        return True
    else:
        return False


def main():
    no_of_coupons = int(input("Enter the number of coupons required : "))
    user_coupon_no = int(input("Enter four digit coupon number: "))
    lucky_coupon_numbers = CouponGenerator.generate_coupon_number(no_of_coupons)

    print("\nLucky Coupons are :")
    for i in range(no_of_coupons):
        print(lucky_coupon_numbers[i], end=" ")

    print("\n")
    for i in range(no_of_coupons):
        if(check_coupon_no(lucky_coupon_numbers[i], user_coupon_no)):
            print(f"\nCongratulations, You are amongst the winner")
            break
    else:
        print(f"\nSorry, your coupon number not in winning list. Better luck next time")


if __name__ == "__main__":
   main()
