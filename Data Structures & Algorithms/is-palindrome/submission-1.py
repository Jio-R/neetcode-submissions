class Solution:
    def isPalindrome(self, s: str) -> bool:
        from string import ascii_letters as a
        x = ''.join(i for i in s if i in a).lower()

        print(x[::-1])
        if x == x[::-1]:
            print(x[::-1])
            return True
        return False