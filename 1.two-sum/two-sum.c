#include <stdio.h>
#include <stdlib.h>
#define PRIME 1009

struct bucket {
  int value;
  struct bucket *next;
};
int hash(int key) { return abs((key % PRIME)); }
void init_ht(struct bucket *ht) {
  int i;
  for (i = 0; i < PRIME; i++) {
    ht[i].value = -1;
    ht[i].next = NULL;
  }
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  int *result = (int *)malloc(sizeof(int) * 2);
  // create hash table
  struct bucket *ht = (struct bucket *)malloc(sizeof(struct bucket) * PRIME);
  init_ht(ht);

  for (int i = 0; i < numsSize; i++) {
    int pos = hash(nums[i]);
    if (ht[pos].value != -1) {
      if (nums[ht[pos].value] == target - nums[i] &&
          ht[pos].value != i) { // get answer
        result[0] = ht[pos].value;
        result[1] = i;
        return result;
      } else {
        struct bucket *t = ht[pos].next;
        while (t) {
          if (nums[t->value] == target - nums[i] &&
              t->value != i) { // get answer
            result[0] = t->value;
            result[1] = i;
            return result;
          } else
            t = t->next;
        }
      }
    }

    int insert_pos = hash(target - nums[i]);
    if (ht[insert_pos].value == -1)
      ht[insert_pos].value = i;
    else { // collision
      struct bucket *new = (struct bucket *)malloc(sizeof(struct bucket));
      new->value = i;
      new->next = ht[insert_pos].next;
      ht[insert_pos].next = new;
    }
  }
  return NULL;
}
