from distutils.dep_util import newer


class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head    #first
            while current.next:
                current = current.next   #next

            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def update(self, index, data):
       current = self.head

       i = 0
       while current:
           if i == index:
               current.data = data
               return True

           i += 1
           current = current.next

       return False


    def delete(self, index):
        current = self.head

        i = 0
        while current:

            if i == index:
                current.data = current.next.data
                return True

            i += 1
            current = current.next


    def add_beggining(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node



ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()
ll.update(1, 50)
ll.display()

