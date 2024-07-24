'''

    @Author: Ayush Prajapati
    @Date: 24-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 24-07-2024 
    @Title : Python program to find the Fewest Notes to be returned for Vending Machine

'''


def vending_machine_change(change, denominations):
    """

    Description:
        This function ginds the Fewest Notes to be returned for Vending Machine
    Parameters:
        change:
        denomination:
    Return:
        float: the elapsed time in seconds

    """
    if change == 0:
        return 0, []

    if change < 0 or not denominations:
        return float('inf'), []

    if change >= denominations[-1]:
        count, notes = vending_machine_change(change - denominations[-1], denominations)
        return count + 1, notes + [denominations[-1]]
    else:
        return vending_machine_change(change, denominations[:-1])


def main():
    denominations = [1, 2, 5, 10, 50, 100, 500, 1000]
    change = int(input("Enter the change amount in Rs: "))
    min_notes, notes_list = vending_machine_change(change, sorted(denominations))

    print(f"Minimum number of notes: {min_notes}")
    print(f"Notes to be returned: {notes_list}")


if __name__ == "__main__":
    main()