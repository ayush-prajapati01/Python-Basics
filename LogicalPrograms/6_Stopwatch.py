'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Simulate Stopwatch

'''


import time


def measure_time():
    """

    Description:
        This function measures the time elapsed between the start and end clicks.
    Parameters:
        None
    Return:
        float: the elapsed time in seconds

    """
    input("Press Enter to start the stopwatch...")
    start_time = time.time()

    input("Press Enter to stop the stopwatch...")
    end_time = time.time()

    elapsed_time = end_time - start_time
    return elapsed_time


def main():
    elapsed_time = measure_time()
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    main()