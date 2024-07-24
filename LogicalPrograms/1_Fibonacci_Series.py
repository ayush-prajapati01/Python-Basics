'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to display the Fibonacci Series

'''

def fibonacci(n):
    """

    Description: 
        This function used to calculate fibonacci series
    Parameters:
        n: It specfies the number of term in the series
    Return:
        int: Element of Fibonacci series

    """
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
  

def main():
    no_of_terms = int(input("Enter the number of terms: "))
    print("Fibonacci Series:")
    for term in range(no_of_terms):
        print(fibonacci(term), end=" ")


if __name__ == "__main__":
   main()

