"""A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:

Input: 

thequickbrownfoxjumpsoverthelazydog

Output: 

true

Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:

Input: 

arvijayakumar

Output: false

Constraints:

1 <= sentence.length <= 1000

sentence consists of lowercase English letters."""

a=input()
flag=0
for i in range(97,123):
    if chr(i) not in a:
        flag=1
        print("false")
        break
if flag!=1:
    print("true")
