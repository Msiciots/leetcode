class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda i: (i[0], i[1]))
        res = []
        for pair in intervals:
            if res and pair[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], pair[1])]
            else:
                res.append(pair)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
