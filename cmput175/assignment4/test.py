from Node import Node

class LinkedList:
    """ The Singly-Linked List class defined in lecture """

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.size

    def add(self, item):
        temp = Node(item, None)
        temp.setNext(self.head)
        self.head = temp
        self.size += 1

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.head
        found = False
        index = 0
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

        self.size -= 1

        return found

    def append(self, item):
        temp = Node(item, None)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(temp)
        self.size += 1

    def pop(self):
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()

        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size -= 1
        return current.getData()

    def getHead(self):
        return self.head
    
    def __str__(self):
        string = ''
        i = 0
        current = self.head
        while current != None:
            dataObject = current.getData()
            if dataObject != None:
                string = string + "%s" % dataObject
                i += 1
            current = current.getNext()
        return string        


word = "banana"

list1 = LinkedList()
for letter in word:
    list1.append(letter)

list2 = LinkedList()
list2.append(list1.getHead().getData())
list1.remove(list1.getHead().getData())
number = list1.length()

for i in range(number):
    insertion_node = list1.getHead()
    list1.remove(list1.getHead().getData())
    current = list2.getHead()
    
    # if the node being inserted is smaller than any nodes in new_linkedList
    if ord(insertion_node.getData()) < ord(current.getData()):
        insertion_node.setNext(list2.getHead())
        list2.head = insertion_node
        list2.size += 1
    else:
        # while there is a next node and the ascii of the next node is still smaller than the node being inserted
        while current.getNext() != None and ord(current.getNext().getData()) < ord(insertion_node.getData()):
            current = current.getNext()
        # if the traversion comes to the last node, which means there is no node larger than the one being inserted
        if current.getNext() == None:
            current.setNext(insertion_node)
            insertion_node.setNext(None)
            list2.size += 1
        # general cases
        else:
            insertion_node.setNext(current.getNext())
            current.setNext(insertion_node)
            list2.size += 1


def edit_distance(str1, str2, len1, len2):
    cost = 0
    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    
    if str1[len2 - 1] == str2[len2 - 1]:
        cost = 0
    else:
        cost = 1
        
    return min(edit_distance(str1, str2, len1 - 1, len2) + 1, \
               edit_distance(str1, str2, len1, len2 - 1) + 1, \
               edit_distance(str1, str2, len1 - 1, len2 - 1) + cost)

print(edit_distance("apple", "aelpp", 5, 5))
print(edit_distance("hockey", "cehkoy", 6, 6))
print(edit_distance("english", "eghilns", 7, 7))
print(edit_distance("orange", "aegnor", 6, 6))
print(edit_distance("coldplay", "acdllopy", 8, 8))
print(len(''))
