class Solution:
    def groupAnagrams(self, strs):
        letter_count = {}
        for s in strs:
            tmp_count = [0] * 26
            for c in s:
                tmp_count[ord(c) - ord('a')] += 1

            if tuple(tmp_count) in letter_count:
                letter_count[tuple(tmp_count)].append(s)
            else:
                letter_count[tuple(tmp_count)] = [s]

        return letter_count.values()
        

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
