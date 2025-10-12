/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

    struct ListNode* sums = malloc(sizeof(struct ListNode));
    struct ListNode* original = sums;
    int carry = 0;
    sums->val = 0;
    sums->next = NULL;
    while (l1 || l2 || carry) {
        int sum = 0;
        sum += carry;
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }

        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }

        
        carry = sum / 10;
        sums->val = sum % 10;
        if (l1 || l2 || carry) {
            sums->next = malloc(sizeof(struct ListNode));
            sums = sums->next;
            sums->val = 0;
            sums->next = NULL;
        }
    }
    return original;
}