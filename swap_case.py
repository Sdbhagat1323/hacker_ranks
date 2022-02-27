"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  
Function Description

Complete the swap_case function in the editor below.

swap_case has the following parameters:

string s: the string to modify
Returns

string: the modified string
Input Format

A single line containing a string .

Constraints


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".
Language
Pypy 2


"""

def swap_case(s):
    r=""
    for i, char in enumerate(s):
        if char.lower() == char:
            r+=char.upper()
        else:
            r+=char.lower()
    # [r+=char.upper() if char.lower() == char else r+=char.lower() for char in s]
    
    return r

def swap_case2(s):
    return s.swapcase()


# print(swap_case("HaxKer"))
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# s = "c"
# print(s.upper())
# print(s.lower())