class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''
        for char in s:
            if char.isalnum():
                word = word + char.lower()
        for i in word:
            for j in word[::-1]:
                if i == j:
                    word = word[0:len(word) - 1]
                else:
                    return False
                break
        return True
