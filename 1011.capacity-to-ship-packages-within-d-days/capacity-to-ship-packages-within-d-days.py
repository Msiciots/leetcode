class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = int((left + right) / 2)
            count_day = 1
            shift_w = 0
            for w in weights:
                shift_w += w
                if shift_w > mid:
                    count_day += 1
                    shift_w = w
            if count_day > days:
                left = mid + 1
            else:
                right = mid
        return left
