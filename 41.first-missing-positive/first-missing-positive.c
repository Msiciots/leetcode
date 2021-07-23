#define SWAP(a, b)( a ^= b, b ^= a, a ^= b )

int firstMissingPositive(int* nums, int numsSize)
{

    for (int i = 0; i < numsSize; i++) {
        int pos = nums[i] - 1;
        if (nums[i] > 0 && nums[i] <= numsSize) {
            if (pos != i && nums[i] != nums[pos]) {
                SWAP(nums[i], nums[pos]);
                i--;
            } else if (pos != i && nums[i] == nums[pos])
                nums[i] = -1;
        } else
            nums[i] = -1;
    }

    for (int i = 0; i < numsSize; i++) {
        if (!__builtin_clz(nums[i]))
            return i + 1;
    }

    return numsSize == 0 ? 1 : numsSize + 1;
}
