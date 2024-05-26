class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self.head

        middle = self.get_middle(self.head)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_util(self.head)
        right = self.merge_sort_util(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        self.head = sorted_list

    def merge_sort_util(self, h):
        if not h or not h.next:
            return h

        middle = self.get_middle(h)
        next_to_middle = middle.next
        middle.next = None

        left = self.merge_sort_util(h)
        right = self.merge_sort_util(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if not head:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, a, b):
        result = None

        if not a:
            return b
        if not b:
            return a

        if a.data <= b.data:
            result = a
            result.next = self.sorted_merge(a.next, b)
        else:
            result = b
            result.next = self.sorted_merge(a, b.next)

        return result

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    if list2:
        tail.next = list2

    return dummy.next


# Створення списків
list1 = LinkedList()
list1.append(1)
list1.append(3)
list1.append(5)

list2 = LinkedList()
list2.append(2)
list2.append(4)
list2.append(6)

print("List 1:")
list1.print_list()

print("List 2:")
list2.print_list()

# Реверсування списку
list1.reverse()
print("Reversed List 1:")
list1.print_list()

# Сортування списку
list1.merge_sort()
print("Sorted List 1:")
list1.print_list()

# Об'єднання двох відсортованих списків
merged_head = merge_sorted_lists(list1.head, list2.head)
merged_list = LinkedList()
merged_list.head = merged_head

print("Merged Sorted List:")
merged_list.print_list()
