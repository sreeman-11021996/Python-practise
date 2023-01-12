from doubly_inked_list_node import Node

class Doubly_Linked_list:
    def __init__(self) -> None:
        self._head = None
    
    def print_forward(self):
        if self._head is None:
            s= "Linked List is Empty"
            print(s)
            return
        
        itr = self._head
        lstr = ''
        while itr:
            lstr += str(itr._data) + "-->" if (itr._next) else str(itr._data)
            itr = itr._next
        print(lstr)
        
    def print_backward(self):
        if self._head is None:
            s= "Linked List is Empty"
            print(s)
            return
        
        itr = self._get_last_node()
        lstr = ''
        while itr:
            lstr += str(itr._data) + "<--" if (itr._prev) else str(itr._data)
            itr = itr._prev
        print(lstr)
        
    def _get_last_node(self):
        itr = self._head
        while itr._next:
            itr = itr._next
        return itr
    
    def get_length(self):
        count=0
        itr = self._head
        while itr:
            count+=1
            itr = itr._next   
        return count
        
    def insert_at_beginning(self,data):
        node = Node(data=data,next=self._head,prev=None)
        if self._head is not None:
            self._head._prev = node
        self._head = node
    
    def insert_at_end(self,data):
        if self._head == None:
            node = Node(data=data,next=self._head,prev=None)
            self._head = node
            return
        
        itr = self._head
        while itr._next:
            itr = itr._next
        itr._next = Node(data=data,next=None,prev=itr)
        
    def insert_at(self,data,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return 

        itr = self._head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data=data,next=itr._next,prev=itr)
                if node._next:
                    node._next._prev = node
                itr._next = node
                break
            itr = itr._next
            count+=1
    
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self._head = self._head._next
            self._head._prev = None
            return
        
        itr = self._head
        count = 0
        while itr:
            if count == index - 1:
                itr._next = itr._next._next
                if itr._next:
                    itr._next._prev = itr
                break
            itr = itr._next
            count+=1
    
    def insert_values(self,data:list):
        self._head = None
        for val in data:
            self.insert_at_end(val)
        
if __name__ == "__main__":
    dll = Doubly_Linked_list()
    dll.insert_at_beginning(5)
    dll.insert_at_beginning(25)
    dll.insert_at_beginning(78)
    dll.insert_at_end(1000)
    dll.insert_at_end(2000)
    dll.print_forward()
    dll.print_backward()
    dll.remove_at(1)
    dll.print_forward()
    dll.print_backward()
    dll.insert_at(50000,2)
    dll.print_forward()
    dll.print_backward()