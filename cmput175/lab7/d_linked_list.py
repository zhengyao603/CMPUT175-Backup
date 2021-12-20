from d_linked_node import d_linked_node

class d_linked_list:
    
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

            
    def search(self, item):
        # search for the desired item from the linked list
        # return a boolean representing whether the item is found
        current = self.__head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
        return found
        
    def index(self, item):
        # search for the index of the desired item
        # return -1 if the item does not exist in the linked list
        # return the actual index if the item exits
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found= True
            else:
                current = current.getNext()
                index = index + 1
        if not found:
                index = -1
        return index        
         
    def add(self, item):
        # adds an item to list at the beginning
        temp = d_linked_node(item, self.__head, None)
        if self.__head != None:
            self.__head.setPrevious(temp)
        else:
            self.__tail = temp
        self.__head = temp
        self.__size += 1
        
    def remove(self, item):
        # search for the item and remove it the method assumes the item exists
        current = self.__head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.__head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if current.getNext() != None:
            current.getNext().setPrevious(previous)
        else:
            self.__tail = previous
        self.__size -= 1
        
    def append(self, item):
        # adds the item to the end of the list
        # must traverse the list to the end and add item
        temp = d_linked_node(item, None, None)
        if self.__head == None:
            self.__head = temp
        else:
            self.__tail.setNext(temp)
            temp.setPrevious(self.__tail)
        self.__tail = temp
        self.__size += 1
        
    def insert(self, pos, item):
        assert 0 <= pos < self.__size, "Position does not exist"
        if pos == 0:
            self.add(item)
        # if the position is not the first index
        else:
            current = self.__head
            index = 0
            while index < pos:
                current = current.getNext()
                index += 1
            temp = d_linked_node(item, current, current.getPrevious())
            self.__size += 1
        
    def pop(self, pos = None):
        if pos == None:
            # if pos is not given, this function will remove the last item of the
            # linked list and return that item
            assert self.__size != 0, "No such element can be poped"
            current = self.__tail
            item = current.getData()
            if self.__size == 1:
                self.__head = None
                self.__tail = None
            elif self.__size > 1:
                current.getPrevious().setNext(None)
                self.__tail = current.getPrevious()
            self.__size -= 1
            return item
        # if pos is given, it will remove the item at given position and return
        # that item
        else:
            if pos == 0:
                item = self.__head.getData()
                if self.__size == 1:
                    self.__head = None
                    self.__tail = None                
                elif self.__size > 1:
                    self.__head.getNext().setPrevious(None)
                    self.__head = self.__head.getNext()
                self.__size -= 1
                return item
            elif pos == self.__size - 1:
                item = self.__tail.getData()
                if self.__size == 1:
                    self.__head = None
                    self.__tail = None
                elif self.__size > 1:
                    self.__tail.getPrevious().setNext(None)
                    self.__tail = self.__tail.getPrevious()
                self.__size -= 1
                return item
            # if the given position is not the first or the last element
            else:
                current = self.__head
                index = 0
                while index < pos:
                    current = current.getNext()
                    index += 1
                item = current.getData()
                current_previous = current.getPrevious()
                current_next = current.getNext()
                current_previous.setNext(current_next)
                current_next.setPrevious(current_previous)
                self.__size -= 1
                return item
            
        
    def search_larger(self, item):
        # This function will return the index of the first number which is
        # larger than the given item
        assert type(item) == int, "Invalid item for comparison"
        current = self.__head
        found = False
        result = 0
        while not found:
            if current == None:
                break
            if current.getData() > item:
                result = self.index(current.getData())
                found = True
            else:
                if current.getNext() == None:
                    break
                else:
                    current = current.getNext()
        if found == True:
            return result
        else:
            return -1
                
        
    def get_size(self):
        # returns the current size of the linked list
        return self.__size
    
    def get_item(self, pos):
        # returns the item at the given position
        # pos can be either positive or negative
        if pos >= 0:
            assert pos < self.__size, "Posistion does not exist"
            current = self.__head
            index = 0
            while index < pos:
                current = current.getNext()
                index += 1
            return current.getData()
        elif pos < 0:
            assert -pos < self.__size + 1, "Position does not exist"
            current = self.__tail
            index = -1
            while index > pos:
                current = current.getPrevious()
                index -= 1
            return current.getData()
        
    def __str__(self):
        # function which allows user to print the string expression of the current linked list
        string = ''
        i = 0
        current = self.__head
        while current != None:
            if i > 0:
                string = string + ' '
            dataObject = current.getData()
            if dataObject != None:
                string = string + "%s" % dataObject
                i += 1
            current = current.getNext()
        return string
        

def test():
                  
    linked_list = d_linked_list()
                    
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    linked_list.add("World")
    linked_list.add("Hello")    
        
    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"
              
    is_pass = (linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.get_item(0) == "Hello")
    assert is_pass == True, "fail the test"
        
    is_pass = (linked_list.get_item(1) == "World")
    assert is_pass == True, "fail the test"    
            
    is_pass = (linked_list.get_item(0) == "Hello" and linked_list.get_size() == 2)
    assert is_pass == True, "fail the test"
            
    is_pass = (linked_list.pop(1) == "World")
    assert is_pass == True, "fail the test"     
    
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"     
            
    is_pass = (linked_list.get_size() == 0)
    assert is_pass == True, "fail the test" 
             
             
            
    int_list2 = d_linked_list()
                    
    for i in range(0, 10):
        int_list2.add(i)      
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"
                
    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    for i in range(21, 23):
        int_list2.insert(0,i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
                
    is_pass = (int_list2.get_size() == 10)
    assert is_pass == True, "fail the test"    
     
     
                    
    int_list = d_linked_list()
                    
    is_pass = (int_list.get_size() == 0)
    assert is_pass == True, "fail the test"
                           
    for i in range(0, 1000):
        int_list.append(i)      
    correctOrder = True
            
    is_pass = (int_list.get_size() == 1000)
    assert is_pass == True, "fail the test"            
    
    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False
                            
    is_pass = correctOrder
    assert is_pass == True, "fail the test" 
            
    is_pass = (int_list.search_larger(200) == 201)
    assert is_pass == True, "fail the test" 
            
    int_list.insert(7,801)
    is_pass = (int_list.search_larger(800) == 7)
    assert is_pass == True, "fail the test"
                 
    is_pass = (int_list.get_item(-1) == 799)
    assert is_pass == True, "fail the test"
            
    is_pass = (int_list.get_item(-4) == 796)
    assert is_pass == True, "fail the test"
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 1! ============")
                
if __name__ == '__main__':
    test()