# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 15:20:16 2023

@author: hamed
"""


class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def enqueue(self, item):
        if len(self.items) == self.capacity:
            raise Exception("Queue is full")
        self.items.append(item)

    def dequeue(self):
        if len(self.items) == 0:
            raise Exception("Queue is empty")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity
    
    def get_length(self):
       return len(self.items)
   
    def  print_queue(self):
        if self.is_empty():
            print("Queue is empty")
       
        else:
            print("Queue:")
            for i in self.items:
                print(i, end=" ")
            print()   
                
queue = Queue(20)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(15)
queue.enqueue(17)
queue.enqueue(14)
queue.dequeue()
print(queue.get_length())
queue.print_queue()       