class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def print_list(self):
        current = self.head
        print('Here is a list:')
        while current:
          print(current.data)
          current = current.next

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def sort(self):
        dummy = Node()
        curr = self.head

        while curr:
            prev = dummy
            next_node = dummy.next

            while next_node and curr.data > next_node.data:
                prev = next_node
                next_node = next_node.next

            prev.next = curr
            temp = curr.next
            curr.next = next_node
            curr = temp

        self.head = dummy.next

def merge_sorted_lists(list1, list2):
    new_list = LinkedList()
    head1 = list1.head
    head2 = list2.head

    while head1 and head2:
        if head1.data < head2.data:
            new_list.insert(head1.data)
            head1 = head1.next
        else:
            new_list.insert(head2.data)
            head2 = head2.next

    if head1:
        while head1:
            new_list.insert(head1.data)
            head1 = head1.next
    elif head2:
        while head2:
            new_list.insert(head2.data)
            head2 = head2.next

    return new_list

llist = LinkedList()

llist.insert(4)
llist.insert(8)
llist.insert(5)
llist.insert(2)
llist.insert(9)
llist.print_list()

llist.reverse()
llist.print_list()
llist.sort()
llist.print_list()

llist2 = LinkedList()
llist2.insert(7)
llist2.insert(3)
llist2.insert(6)
llist2.insert(4)
llist2.sort()

merged_list = merge_sorted_lists(llist, llist2)
merged_list.print_list()
