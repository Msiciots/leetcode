# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

### Categorize by Count
Time: O(NK)
Space: O(NK)
count the letter and throw to a hash map
```python3
count = {
    (2, 1, 0, 0, ..., 0): ["aab", "aba", "baa"], 
    (1, 2, 3, 0, 0, ..., 0): ["abbccc"]
}
```
