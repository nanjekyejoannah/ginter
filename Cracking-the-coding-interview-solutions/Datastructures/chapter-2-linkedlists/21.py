def removeDuplicates(head):
    curr = head
    dups ={}
    while curr is not None:
        if dups.has_key(curr.value):
            if curr.prev is not None:
                curr.prev.next = curr.next
            if curr.next is not None:
                curr.next.prev = curr.prev
            temp = curr
            curr = curr.next
            del temp
        else:
            dups[curr.value] = True
            curr = curr.next