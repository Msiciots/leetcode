class Solution:
    def characterReplacement(self, s: str, k: int):
        count_letter = [0] * 26
        l = 0 
        max_letter = 0
        for r in range(len(s)):
            count_letter[ord(s[r]) - ord('A')] += 1
            max_letter = max(max_letter, count_letter[ord(s[r]) - ord('A')])
            if r - l + 1 > max_letter + k:
                count_letter[ord(s[l]) - ord('A')] -= 1
                l += 1
        return len(s) - l # Because the window will remain max length
            
            
