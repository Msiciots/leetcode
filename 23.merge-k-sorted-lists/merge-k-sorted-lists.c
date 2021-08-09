/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
void swap(struct ListNode** heap, int i, int j) {
  struct ListNode* tmp = heap[i];
  heap[i] = heap[j];
  heap[j] = tmp;
}
void print_heap(struct ListNode** heap, int heap_count) { // For debug
  int i = 1;
  printf("Heap:");
  while (i <= heap_count) printf("%d ", heap[i++]->val);
  printf("\n");
}

void heapify(struct ListNode** heap, int i, int heap_count) {
  if (!heap_count) return;
  int comp_index;
  if (2 * i > heap_count)  // No child
    return;
  else if (2 * i + 1 > heap_count)  // Only left child
    comp_index = 2 * i;
  else
    comp_index = heap[2 * i]->val < heap[2 * i + 1]->val ? 2 * i : 2 * i + 1;

  if (heap[i]->val > heap[comp_index]->val) {
    swap(heap, i, comp_index);
    heapify(heap, comp_index, heap_count);
  }
}
void build_min_heap(struct ListNode** heap, int heap_count) {
  for (int i = heap_count / 2; i >= 1; i--)
    heapify(heap, i, heap_count);
}
struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
  struct ListNode* heap[listsSize + 1];
  if (!listsSize) return NULL;
  int heap_count = 0;
  for (int i = 0; i < listsSize; i++) {
    if (!lists[i]) continue;
    heap_count++;
    heap[heap_count] = lists[i];
  }
  if (!heap_count) return NULL;
  build_min_heap(heap, heap_count);
  struct ListNode* head = NULL;
  struct ListNode* tail = NULL;
  do {
    struct ListNode* pop_min = heap[1];
    if (!head)
      head = tail = pop_min;
    else
      tail = tail->next = pop_min;
    if (pop_min->next)
      heap[1] = heap[1]->next;
    else {
      swap(heap, 1, heap_count);
      heap_count--;
    }
    heapify(heap, 1, heap_count);
  } while (heap_count);

  return head;
}