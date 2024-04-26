def reverse_linked_list(head): # Time complexity:
    # Base case
    if head is None or head.next is None:
        return head

    # Recursive case
    pivot = reverse_linked_list(head.next)
    head.next.next = head
    head.next = None

    return pivot

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linked_list(head):
    while head:
        print(head.val, end="")
        head = head.next
        if head:
            print(" -> ", end="")

node = Node(
    1,
    Node(
        2,
        Node(
            3,
            Node(
                4,
                Node(
                    5,
                    Node(6)
                )
            )
        )
    )
)



print_linked_list(node)
node = reverse_linked_list(node)
print('')
print_linked_list(node)
