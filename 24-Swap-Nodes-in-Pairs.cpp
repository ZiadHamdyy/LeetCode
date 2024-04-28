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
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head == NULL || head->next == NULL){
            return head;
        }
        ListNode *tempNode = new ListNode();
        tempNode->next = head;
        ListNode *ptr = tempNode, *first, *second;
        while(ptr->next != NULL && ptr->next->next != NULL){
            ListNode *first = ptr->next;
            ListNode *second = ptr->next->next;
            ptr->next = second;
            first->next = second->next;
            second->next = first;
            ptr = first;
        }
        return tempNode->next;
    }
};