# [Leetcode 1. Two Sum](https://leetcode.com/problems/two-sum/)

Example:
```
Input: nums = [3,6,5,1,1010], target = 7
Output: [1,3]
```
Use **hash table**, because search key in hash table is O(1) time.  
In python, just store data to dictionary. 
```
key = target - nums[i]  
value = i
and check the coming nums[i] is in dict or not.
```
| key | value |
| -------- | -------- | 
| 4     |  -1    |  
| 1     |  1    |  
| 2     |  2    |  
| 6     |  -1    |  
| -1003     |  0    |   

In C, you need to build hash table by youself.  
`H(x) = (target - nums[i]) mod 1009`
| key | value |next value |
| -------- | -------- | -------- | 
| 0     |  -1    |    NULL    | 
| 1     |  1    |   4    | 
| 2     |  2    |   NULL    |
| 3     |  -1    |   NULL    |
| 4     |  0    |   NULL    |
| 5     |  0    |   NULL    |
| 6     |  3    |   NULL    |