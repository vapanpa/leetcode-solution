object Solution {
    def removeElements(head: ListNode, `val`: Int): ListNode = {
        if (head == null) {
            return head
        } else if (head.x == `val`) {
            return removeElements(head.next, `val`)
        } else {
            head.next = removeElements(head.next, `val`)
            return head
        }
    }
}
