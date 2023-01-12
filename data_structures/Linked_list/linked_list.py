from linked_list_node import Node

class Linked_list:
    def __init__(self) -> None:
        self._head = None
        
    def __str__(self):
        if self._head is None:
            s= "Linked List is Empty"
            return s
        
        itr = self._head
        lstr = ''
        while itr:
            lstr += str(itr._data) + "-->" if (itr._next) else str(itr._data)
            itr = itr._next
        return lstr
        
    def get_length(self):
        count=0
        itr = self._head
        while itr:
            count+=1
            itr = itr._next   
        return count
    
    def insert_at_beginning(self,data):
        node = Node(data=data,next=self._head)
        self._head = node
        
    def insert_at_end(self,data):
        if self._head is None:
            self._head = Node(data=data,next=None)
            return 
        itr = self._head
        while itr._next:
            itr = itr._next
        itr._next = Node(data=data,next=None)
        
    def insert_at(self,data,index:int):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return 
        
        itr = self._head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data=data,next=itr._next)
                itr._next = node
                break
            itr = itr._next
            count+=1
    
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self._head = self._head._next
            return
        
        itr = self._head
        count = 0
        while itr:
            if count == index - 1:
                itr._next = itr._next._next
                break
            itr = itr._next
            count+=1
    
    def insert_values(self,data:list):
        self._head = None
        for val in data:
            self.insert_at_end(val)
            
    def insert_after_value(self, data_after, data_to_insert):
        # Search for first occurance of data_after value in linked list
        if self._head is None:
            raise Exception(self.__str__())
        
        itr = self._head
        index = 0
        value_not_found = True 
        while itr:
            if itr._data == data_after:
                index = index + 1
                value_not_found = False
                break
            itr = itr._next
            index += 1
        
        if value_not_found:
            raise Exception("Value not Found")
        
        # Now insert data_to_insert after data_after node
        self.insert_at(data=data_to_insert,index=index)

    def remove_by_value(self, data):
        # Remove first node that contains data
        if self._head is None:
            raise Exception(self.__str__())
        
        itr = self._head
        index = 0
        value_not_found = True 
        while itr:
            if itr._data == data:
                value_not_found = False
                break
            itr = itr._next
            index += 1
        
        if value_not_found:
            raise Exception("Value not Found")

        # Remove first node that contains data
        self.remove_at(index=index)
            
if __name__ == "__main__":
    ll = Linked_list()
    ll.insert_at_beginning(45)
    ll.insert_at_beginning(5)
    ll.insert_at_end(9)
    print(ll)
    ll.insert_at(78,2)
    print(ll)
    ll.insert_after_value(78,1000)
    print(ll)
    ll.remove_by_value(5)
    print(ll)