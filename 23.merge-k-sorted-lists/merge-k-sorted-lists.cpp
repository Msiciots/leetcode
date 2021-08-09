/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
#include <iostream>
#include <vector>
using namespace std;

struct greater1 {
  bool operator()(ListNode* a, ListNode* b) const { return a->val > b->val; }
};

class Solution {
 public:
  ListNode* mergeKLists(vector<ListNode*>& lists) {
    vector<ListNode*> heap;
    for (auto node : lists) {
      if (!node) continue;
      heap.push_back(node);
    }
    if (heap.empty()) return NULL;
    make_heap(heap.begin(), heap.end(), greater1());

    struct ListNode* head = NULL;
    struct ListNode* tail = NULL;

    while (!heap.empty()) {
      pop_heap(heap.begin(), heap.end(), greater1());
      ListNode* pop_node = heap.back();
      heap.pop_back();
      if (!head)
        head = tail = pop_node;
      else {
        tail = tail->next = pop_node;
      }
      if (pop_node->next) {
        heap.push_back(pop_node->next);
        push_heap(heap.begin(), heap.end(), greater1());
      }
    }

    return head;
  }
};