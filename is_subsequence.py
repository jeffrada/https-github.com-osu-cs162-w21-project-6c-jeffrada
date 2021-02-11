# Author: Adam Jeffries
# Date: 2/9/2021
# Description: A recursive function named is_subsequence that takes two string parameters
# and returns True if the first string is a subsequence of the second string, but returns False otherwise.

def is_subsequence(string1, string2):
    if string1 == "":
        return True
    if string2 == "":
        return False
    if string1[0] == string2[0]:
        return is_subsequence(string1[1:], string2[1:])
    else:
        return is_subsequence(string1, string2[1:])
