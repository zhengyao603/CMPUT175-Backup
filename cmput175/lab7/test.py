        if self.__ifsort == True:
            self.__sortitems.append(item)
            self.__sortitems.sort()
            correct_pos = self.__sortitems.index(item)
            if correct_pos == 0:
                temp = d_linked_node(item, self.__head, None)
                if self.__head != None:
                    self.__head.setPrevious(temp)
                else:
                    self.__tail = temp
                self.__head = temp
            elif correct_pos == self.__size - 1:
                temp = d_linked_node(item, None, None)
                if self.__head == None:
                    self.__head = temp
                else:
                    self.__tail.setNext(temp)
                    temp.setPrevious(self.__tail)
                self.__tail = temp
            else:
                current = self.__head
                index = 0
                while index < correct_pos:
                    current = current.getNext()
                    index += 1
                temp = d_linked_node(item, current.getNext(), current.getPrevious())
                current.getNext().setPrevious(temp)
                current.getPrevious().setNext(temp)
        
        
        elif self.__ifsort == False:
            temp = d_linked_node(item, None, None)
            if self.__head == None:
                self.__head = temp
            else:
                self.__tail.setNext(temp)
                temp.setPrevious(self.__tail)
            self.__tail = temp

        self.__size += 1
        
    def pop(self):
        assert self.__size != 0, "No such element can be poped"
        if self.__ifsort == True:
            largest = 0
            for item in self.__sortitems:
                if item > largest:
                    largest = item
            correct_pos = self.__sortlist.index(largest)
            self.__sortitems.pop(correct_pos)
            current = self.__head
            index = 0
            while index < correct_pos:
                current = current.getNext()
                index += 1
            current_next = current.getNext()
            current_previous = current.getPrevious()
            current_next.setPrevious(current_previous)
            current_previous.setNext(current_next)
        
        
        elif self.__ifsort == False:
            current = self.__head
            item = self.__head.getData()
            if self.__size == 1:
                self.__head = None
                self.__tail = None
            elif self.__size > 1:
                current.getNext().setPrevious(None)
                self.__head = current.getNext()
            return item
        
        self.__size -= 1
         
    def search(self, item):
        current = self.__head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index += 1
        
        if self.__ifsort == True:
            if found == True:
                return (True, index)
            else:
                larger_index = 0
                larger = self.__head
                larger_found = False
                while larger != None and larger_found == False:
                    if larger.getData() > item:
                        larger_found = True
                    else:
                        larger = larger.getNext()
                        larger_index += 1
                if larger_found == True:
                    return (False, larger_index)
                else:
                    return (False, -1)
        
        elif self.__ifsort == False:
            return (False, -1)
        
        
    def change_sorted(self):
        if self.__ifsort == True:
            self.__ifsort == False
        elif self.__ifsort == False:
            raise Exception("I don’t know how to sort a doubly linked list yet")
        
    def get_size(self):
        return self.__size
        
    def get_item(self, pos):
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
                  
    sor_list = m_sorted_list(True)
                    
    is_pass = (sor_list.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    sor_list.add(4)
    sor_list.add(3)
    sor_list.add(8)
    sor_list.add(7)
    sor_list.add(1)
               
    is_pass = (str(sor_list) == "1 3 4 7 8")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list.get_size() == 5)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list.pop() == 8)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list.pop() == 7)
    assert is_pass == True, "fail the test"
    
    is_pass = (str(sor_list) == "1 3 4")
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == 1)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(3)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(7)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    is_pass = (sor_list.get_size() == 3)
    assert is_pass == True, "fail the test"  
    
    is_pass = (sor_list.get_item(2) == 4)
    assert is_pass == True, "fail the test"      
    
    sor_list.change_sorted()
    
    sor_list.add(1)
               
    is_pass = (str(sor_list) == "1 3 4 1")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list.pop() == 1)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list.pop() == 3)
    assert is_pass == True, "fail the test"
    
    sor_list.add(7)
    sor_list.add(6)
    
    is_pass = (str(sor_list) == "4 1 7 6")
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(7)
    is_pass = (a[0] == True and a[1] == 2)
    assert is_pass == True, "fail the test"
    
    a = sor_list.search(8)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    is_pass = (sor_list.get_size() == 4)
    assert is_pass == True, "fail the test"  
    
    is_pass = (sor_list.get_item(2) == 7)
    assert is_pass == True, "fail the test"      
      
    
    sor_list2 = m_sorted_list(False)
                    
    is_pass = (sor_list2.get_size() == 0)
    assert is_pass == True, "fail the test"
            
    sor_list2.add(4)
    sor_list2.add(3)
    sor_list2.add(8)
    sor_list2.add(7)
    sor_list2.add(1)
               
    is_pass = (str(sor_list2) == "4 3 8 7 1")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 4)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 3)
    assert is_pass == True, "fail the test"
    
    is_pass = (str(sor_list2) == "8 7 1")
    assert is_pass == True, "fail the test"
    
    a = sor_list2.search(2)
    is_pass = (a[0] == False and a[1] == -1)
    assert is_pass == True, "fail the test"
    
    a = sor_list2.search(7)
    is_pass = (a[0] == True and a[1] == 1)
    assert is_pass == True, "fail the test"
    
    is_pass = (sor_list2.get_size() == 3)
    assert is_pass == True, "fail the test"  
    
    is_pass = (sor_list2.get_item(2) == 1)
    assert is_pass == True, "fail the test"      
    
    try:
        sor_list2.change_sorted()
    except Exception as e:
        is_pass = True
    else:
        is_pass = False
    assert is_pass == True, "fail the test"    
    
    
    sor_list2.add(3)
    sor_list2.add(2)
               
    is_pass = (str(sor_list2) == "8 7 1 3 2")
    assert is_pass == True, "fail the test"
                
    is_pass = (sor_list2.get_size() == 5)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 8)
    assert is_pass == True, "fail the test"
        
    is_pass = (sor_list2.pop() == 7)
    assert is_pass == True, "fail the test"
    
    
    is_pass = (str(sor_list2) == "1 3 2")
    assert is_pass == True, "fail the test"
    
                    
    if is_pass == True:
        print ("=========== Congratulations! Your have finished exercise 2! ============")
                
if __name__ == '__main__':
    test()
