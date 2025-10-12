/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode * temp = head;
    if (!head) {
        return NULL;
    }
    while (temp->next) {
        if (temp->val == temp->next->val) {
            if (head->next->next) {
                struct ListNode * delete = temp->next;
                
                temp->next = temp->next->next;
                free(delete);
            } else {
                temp->next = NULL;
            }
        } else {
            temp = temp->next;
        }
    }
    return head;

}