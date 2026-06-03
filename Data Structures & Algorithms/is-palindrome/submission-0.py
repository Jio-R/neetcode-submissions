class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = ''.join(i for i in s if i.isalpha()).lower()

        print(x[::-1])
        if x == x[::-1]:
            print(x[::-1])
            return True
        return False