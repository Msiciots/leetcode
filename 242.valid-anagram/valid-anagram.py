class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letter = [0] * 26
        
        for char in s:
            letter[ord(char) - ord('a')] += 1

        for char in t:
            letter[ord(char) - ord('a')] -= 1

        for l in letter:
            if l != 0:
                return False

        return True
            

