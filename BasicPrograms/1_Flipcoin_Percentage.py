'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Flip Coin and print percentage of Heads and Tails

'''


import random


def calc_heads_tails_percentage(no_of_coin_flips):
    """

    Description: 
        This function used to calculate heads and tails percentage
    Parameters:
        no_of_coin_flips: It specifies no of times coin has to be flipped
    Return:
        None

    """
    if (no_of_coin_flips > 0):
        heads = 0
        tails = 0
        for _ in range(no_of_coin_flips):
            if (random.random() < 0.5):
                tails += 1
            else:
                heads += 1

        # Printing and calculating percentage
        print(f"Percentage of Heads: {(heads/no_of_coin_flips)*100:.2f} %")
        print(f"Percentage of Heads: {(tails/no_of_coin_flips)*100:.2f} %")

    else:
        print("Please enter a positive integer.")


def main():
    no_of_coin_flips = int(input("Enter number of times to Flip Coin: "))
    calc_heads_tails_percentage(no_of_coin_flips)


if __name__ == "__main__":
    main()