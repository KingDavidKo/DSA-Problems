/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode * output = malloc(sizeof(struct ListNode));
    struct ListNode * start = output;
    if (!list1 && !list2) {
        free(output);
        return NULL;
    } else if (!list1) {
        free(output);
        return list2;
    } else if (!list2) {
        free(output);
        return list1;
    }
    while (list1 && list2) {
        if (list1->val <= list2->val) {
            output->val = list1->val;
            list1 = list1->next;
        } else {
            output->val = list2->val;
            list2 = list2->next;
        }
        if (list1 && list2) {
            output->next = malloc(sizeof(struct ListNode));
            output = output->next;
        }
    }
    if (list1) {
        output->next = list1;
    } else {
        output->next = list2;
    }
    return start;
}