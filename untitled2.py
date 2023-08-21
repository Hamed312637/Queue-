# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:36:56 2023

@author: hamed
"""




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if self.head is None:
            raise Exception("Queue is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def is_empty(self):
        return self.head is None

    def get_length(self):
       if self.head is None:
         return 0

       length = 1
       node = self.head
       while node.next is not None:
          length += 1
          node = node.next

       return length

    def print_queue(self):
        if self.head is None:
            print("Queue is empty")
            return

        node = self.head
        print("Queue:")
        while node is not None:
            print(node.data, end=" ")
            node = node.next
        print()
                
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(15)
queue.enqueue(17)
queue.enqueue(14)
queue.dequeue()
print(queue.get_length())
queue.print_queue()         