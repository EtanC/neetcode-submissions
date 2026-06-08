/**
 * Definition for singly-linked list.
 * class ListNode {
 *     constructor(val = 0, next = null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

class Solution {
    /**
     * @param {ListNode} list1
     * @param {ListNode} list2
     * @return {ListNode}
     */
    mergeTwoLists(list1, list2) {
        let curr1 = list1;
        let curr2 = list2;
        const head = new ListNode();
        head.val = NaN;
        head.next = null;
        let curr = head;

        while (curr1 && curr2) {
            if (curr1.val <= curr2.val) {
                curr.next.val = curr1.val;
                curr1 = curr1.next;
            } else {
                curr.next.val = curr2.val;
                curr2 = curr2.next;
            }
            curr.next = null
        }
        return head;
    }
}
