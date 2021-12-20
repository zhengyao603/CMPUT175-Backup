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

class SecretWord:

    def __init__(self):
        self.linkedList = LinkedList()

        # Additional attribute(s) go here:
        

    def setWord(self, word):
        """ Adds the characters in 'word' to self.linkedList in the given order """
        #TODO: adds all the lettes from given word into linked list and initialize
        # the gameProgress attribute
        for letter in word:
            self.linkedList.append(letter)
        

    def sort(self):
        """ Sorts the characters stored in self.linkedList in alphabetical order """
        #TODO: using insertion sort to sort the word in alphabetical order
        new_linkedList = LinkedList()
        # insert the head of original linkedlist into new list and remove
        # the head of the original linkedlist
        new_linkedList.append(self.linkedList.getHead().getData())
        self.linkedList.remove(self.linkedList.getHead().getData())
        number_for_insertion = self.linkedList.length()
        
        # insert all the left nodes into new linkedlist by insertion sort
        for i in range(number_for_insertion):
            insertion_node = self.linkedList.getHead()
            self.linkedList.remove(self.linkedList.getHead().getData())
            current = new_linkedList.getHead()
            
            # if the node being inserted is smaller than any nodes in new_linkedList
            if ord(insertion_node.getData()) < ord(current.getData()):
                insertion_node.setNext(new_linkedList.getHead())
                new_linkedList.head = insertion_node
                new_linkedList.size += 1
            else:
                # while there is a next node and the ascii of the next node is still smaller than the node being inserted
                while current.getNext() != None and ord(current.getNext().getData()) < ord(insertion_node.getData()):
                    current = current.getNext()
                # if the traversion comes to the last node, which means there is no node larger than the one being inserted
                if current.getNext() == None:
                    current.setNext(insertion_node)
                    insertion_node.setNext(None)
                    new_linkedList.size += 1
                # general cases
                else:
                    insertion_node.setNext(current.getNext())
                    current.setNext(insertion_node)
                    new_linkedList.size += 1
        
        self.linkedList = new_linkedList


    def isSolved(self):
        """ Returns whether SecretWord has been solved (all letters in the word have been guessed by the user) """
        #TODO: return True if all the letters are guessed correctly, return False otherwise
        is_solved = True
        current = self.linkedList.getHead()
        # if there is any nodes that cannot be displayed, then return false
        while current != None:
            if not current.getDisplay():
                is_solved = False
            current = current.getNext()
        if is_solved:
            return True
        else:
            return False
        

    def update(self, guess):
        """ Updates the nodes in self.linkedList that match 'guess' """
        #TODO: update current game progress if guess matches any of the letters in the word
        correct_guess = False
        current = self.linkedList.getHead()
        # update all the nodes which match the given parameter guess
        while current != None:
            if current.getData() == guess:
                current.setDisplay(True)
                correct_guess = True
            current = current.getNext()
        # return true if the game progress has been updated
        return correct_guess

    def printProgress(self):
        """ Prints the current game progress
        Ex: y _ l l _ w """
        #TODO: print the current game progress
        gameProgress = ""
        current = self.linkedList.getHead()
        while current != None:
            # if the current node can be displayed
            if current.getDisplay():
                gameProgress += current.getData()
                gameProgress += ' '
            # if the current node cannot be displayed
            else:
                gameProgress += '_'
                gameProgress += ' '
            current = current.getNext()
        print(gameProgress)
        

    def __str__(self):
        """ Converts the characters in self.linkedList into a string """
        #TODO: return string representation of the sorted linked list
        string = ''
        i = 0
        current = self.linkedList.getHead()
        while current != None:
            dataObject = current.getData()
            if dataObject != None:
                string = string + "%s" % dataObject
                i += 1
            current = current.getNext()
        return string
