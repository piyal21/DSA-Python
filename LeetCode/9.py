class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are never palindrome
        if x < 0:
            return False
        
        s = str(x)
        
        def check(a, l, r):
            if l >= r:
                return True
            if a[l] != a[r]:
                return False
            return check(a, l + 1, r - 1)
        
        return check(s, 0, len(s) - 1)
