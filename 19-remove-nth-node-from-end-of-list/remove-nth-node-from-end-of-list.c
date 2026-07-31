/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    struct ListNode * temp=head;
    int c=1;
    while(temp->next!=NULL)
    {
        temp=temp->next;
        c++;


    }
    if (c == n) {
        head = head->next;
        return head;
    }
    temp=head;
    int q=c-n-1;
    int i;
    for(i=0;i<q;i++)
    {
        temp=temp->next;
    }
    temp->next=temp->next->next;
    return head;
    





    
}