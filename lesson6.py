class Node:
    '''
    An object for storing a stingly node of a linked list.
    Models two attributes - data and the link to the next node in the list
    '''
    data = None
    next_node = None

    def __init__(self, data) -> None:
        self.data = data

    def __repr__(self) -> str:
        return f"<Node :: {self.data}>"
    

class LinkedList:
    '''
    Stingly linked list
    '''
    def __init__(self) -> None:
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        '''
        Return the size of node in linked list 
        takes linear time
        '''
        current = self.head
        count = 0
        while current:
            count += 1    
            current = current.next_node
        
        return count
    
    def add_node(self, data):
        '''
        Add a new node containing data
        this takes constant time
        '''
        new_node = Node(data)
        current = self.head
        new_node.next_node = current
        self.head = new_node

    def search(self, target):
        '''
        Returns first node if target is found in the linked list else returns None
        Takes linear time
        '''
        current = self.head
        while current:
            if current.data == target:
                return current
            current = current.next_node

        return None
    
    def insert(self, data, position):
        '''
        Inserts a new node at an index position
        This takes constant time but finding a node takes linear time

        Therefore, overall complexity time is linear time
        '''
        if position == 0:
            self.add_node(data)
        current = self.head
        new_node = Node(data)
        count = 1
        while count <= position:
            if count == position:
                successor_node = current.next_node
                current.next_node = new_node
                new_node.next_node = successor_node
            current = current.next_node    
            count += 1
        return current   

    def remove(self, position):
        '''
        Removes node at the index position
        Takes linear time
        '''
        if self.size() == 0:
            return None
        elif self.size() == 1:
            self.head = None
            return self
        else:
            current = self.head 
            prev_node = None
            while position > 0:
                if position == 1 and current is not None:    
                    prev_node.next_node = current.next_node
                prev_node = current
                current = current.next_node
                position -= 1
            return current
                
        
    
    def __repr__(self) -> str:
        '''
        Returns string representation of the list
        Takes a linear time
        '''
        current = self.head
        nodes = []
        while current:
            indicator = ''
            if self.head == current:
                indicator = 'Head: '
            elif current.next_node == None:
                indicator = "Tail: "
            else:
                indicator = ''
            nodes.append(f"{indicator}{current.data}")
            current = current.next_node
        return " -> ".join(nodes)
    

        