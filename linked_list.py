class Node:
    """
    An object for stroring data in a linked list.
    Models two attributes: data and next_node.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data   
    
class LinkedList:
        """
        singly linked list.
        """  

        def __init__(self):
                self.head = None

        def is_empty(self):
                """
                Returns True if the linked list is empty, otherwise False.
                """
                return self.head is None
    
                """
                Returns the number of nodes in the list, takes linear time
                """
        def size(self):
                current = self.head
                count = 0

                while current:
                        count += 1
                        current = current.next_node
                return count
        
        def add(self, data):
               
               """
               Adds a new node with the specified data to the beginning of the list.
               """
               new_node = Node(data)
               new_node.next_node = self.head
               self.head = new_node

        def search(self, key):
                """
                Searches for the first node with the specified data ('key' value).
                Returns the node if found, otherwise None.
                Takes linear time
                """
                current = self.head

                while current:
                        if current.data == key:
                                return current
                        
                        else:
                               current = current.next_node
                return None
        
        def insert(self, data, index):
                """
                Inserts a new node with the specified data at the given index.
                Takes linear time
                """
                if index == 0:
                        self.add(data)
                        
                if index > 0:
                       new = Node(data)

                       position = index
                       current = self.head
                
                       while position > 1:
                        current = current.next_node
                        position -= 1

                prev_node = current
                next_node = current.next_node

                prev_node.next_node = new
                new.next_node = next_node
        
        def remove(self, key):
                """
                Removes the first node with the specified data ('key' value).
                If key doesnt exist, returns None.
                Takes linear time
                """
                current = self.head
                previous = None
                found = False
                while current and not found:
                        if current.data == key and current is self.head:
                                found = True
                                self.head = current.next_node
                        elif current.data == key:
                                found == True
                                previous.next_node = current.next_node
                        else:    
                                previous = current
                                current = current.next_node
                return current 

        def __repr__(self):
                """
                Returns a string representation of the linked list.
                Takes linear time
                """
                nodes = []
                current = self.head
                        
                while current:
                        if current is self.head:
                                nodes.append("[Head: %s]" % current.data)
                        elif current.next_node is None:
                                nodes.append("[Tail: %s]" % current.data)
                        else:
                                nodes.append("[%s]" % current.data)
                        
                        current = current.next_node
                return '-> '.join(nodes)
