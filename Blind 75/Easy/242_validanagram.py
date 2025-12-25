"""
LeetCode 242 - Valid Anagram

Instructions:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word 
or phrase, typically using all the original letters exactly once.

Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

Example 2:
    Input: s = "rat", t = "car"
    Output: false

Constraints:
    - 1 <= s.length, t.length <= 5 * 10^4
    - s and t consist of lowercase English letters.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


    def compare_anagrams()
        
        




t_string= input("Type the first string : ").lower().replace(" ","")
s_string= input("Type the second string (to compare) : ").lower().replace(" ","")

lenght = len(t_string)
backwards_t = []



for i in range( lenght-1,-1,  -1 ):
    backwards_t = backwards_t.append(s_string[i])
    

if (backwards_t == s_string):
    return True
else:
    return False


print()