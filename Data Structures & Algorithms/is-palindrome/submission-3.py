class Solution:
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_letters as a, digits as d

        x = ''.join(i for i in s if i in a+d).lower()

        if x == x[::-1]:
            return True
        return False
        