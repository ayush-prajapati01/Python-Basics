'''

    @Author: Ayush Prajapati
    @Date: 23-07-2024
    @Last Modified by: Ayush Prajapati
    @Last Modified time: 23-07-2024 
    @Title : Python program to Check Whether an Alphabet is Vowel or Consonant

'''


def check_vowel(char):
    """

    Description: 
        This function used to check whether an Alphabet is Vowel or not
    Parameters:
        char: The aplhabet to be checked
    Return:
        boolean: Whether vowel

    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    if char in vowels:
        return True
    else:
        return False
  

def main():
    char = input("Enter a character: ")
    char = char[0].lower()
    if check_vowel(char):
        print(f"{char} is a Vowel")
    else:
        print(f"{char} is a Consonant")


if __name__ == "__main__":
    main()

