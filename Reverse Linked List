/**
 * Definition for singly-linked list.
 * class ListNode(_x: Int = 0, _next: ListNode = null) {
 *   var next: ListNode = _next
 *   var x: Int = _x
 * }
 */
object Solution {
    def reverseList(head: ListNode): ListNode = {
        def rev(list: ListNode, buildList: ListNode): ListNode =
            if (list == null){
                buildList
            }
            else{
                rev(list.next, ListNode(list.x, buildList))
            }
        rev(head, null)
    }
}
