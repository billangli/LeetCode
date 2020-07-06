/* AddTwoNumbers

 Created by Bill Li on 1/2/2018.
 */

package medium;

public class AddTwoNumbers {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        int sum = l1.val + l2.val;
        ListNode result = new ListNode(sum % 10);
        int carry = sum / 10;

        ListNode n1 = l1.next;
        ListNode n2 = l2.next;
        ListNode r = result;

        while ((n1 != null) && (n2 != null))  {
            sum = n1.val + n2.val + carry;
            ListNode n = new ListNode(sum % 10);
            r.next = n;
            r = r.next;
            carry = sum / 10;

            n1 = n1.next;
            n2 = n2.next;
        }

        if (n1 != null) {
            while (n1 != null) {
                sum = n1.val + carry;
                ListNode n = new ListNode(sum % 10);
                r.next = n;
                r = r.next;
                n1 = n1.next;
                carry = sum / 10;
            }
        } else if (n2 != null) {
            while (n2 != null) {
                sum = n2.val + carry;
                ListNode n = new ListNode(sum % 10);
                r.next = n;
                r = r.next;
                n2 = n2.next;
                carry = sum / 10;
            }
        }
        if (carry != 0) {
            ListNode n = new ListNode(carry);
            r.next = n;
        }

        return result;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
