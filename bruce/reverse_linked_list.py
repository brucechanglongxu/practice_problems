# Given the head of a singly linked list, reverse the list, and return the reversed list. 

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:
  # Function to initialize head 
  def __init__(self):
    self.head = None
    
  # Function to reverse the linked list
  def reverse(self):
    prev = None
    current = self.head 
    while(current is not None):
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
    
 # Function to insert a new node at the beginning
 def push(self, new_data);
    new_node = Node(new_data)
    new_node.next = self.head
    self.head = new_node
    
 def printList(self):
    temp = self.head
    while(temp):
      print temp.data
      temp = temp.next
