class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(i for i in s if i.isalnum()).lower()

        if x == x[::-1]:
            return True
        return False
