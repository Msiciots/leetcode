#include <stdio.h>
#include <stdlib.h>
#include "two-sum.c"
int main(int argc, char *argv[]) {
  // int nums[] = {3, 6, 5, 1, 8};
  int nums[] = {2, 7, 11, 15};
  // int *result = (int *)malloc(sizeof(int)*2);
  // twoSum(nums,5,7,&result);
  int returnSize = 2;

  // int *result = twoSum(nums, 5, 7, &returnSize);
  int *result = twoSum(nums, 4, 9, &returnSize);
  for (int i = 0; i < 4; i++) {
    printf("%d ", nums[i]);
  }
  printf("\n%d\n", 9);
  printf("%d,%d\n", result[0], result[1]);
  return 0;
}