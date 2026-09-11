class Solution:
    def isPalindrome(self, s: str) -> bool:
        sNew = "".join([char for char in s if char.isalnum()]).replace(" ", "").lower()

        for i in range(len(sNew)//2):
            if sNew[i] != sNew[-(i+1)]:
                return False
        
        return True