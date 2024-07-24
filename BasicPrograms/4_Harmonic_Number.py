'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to print Nth Harmonic Number

'''

def harmonic_number(n):
    """

    Description: 
        This function used to Nth harmonic number
    Parameters:
        n: It specfies the number of term of harmonic series
    Return:
        int
            Nth harmonic number

    """
    sum = 0
    for i in range(1, n+1):
        sum += 1/i
    return sum


def main():
    n = int(input("Enter the value of N: "))
    if (n != 0):
        harmonic_sum = harmonic_number(n)
        print(f"The Nth Harmonic Value is: {harmonic_sum:.3f}")
    else:
        print("Please enter a non-zero value.")


if __name__ == "__main__":
    main()