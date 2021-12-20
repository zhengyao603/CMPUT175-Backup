class Node:
    def __init__(self, initData, initNext):
        """ Constructs a new node and initializes it to contain
        the given object (initData) and link to the given next node. """
        
        self.data = initData
        self.next = initNext

        # Additional attributes
        self.display = False

    def getData(self):
        """ Returns the element """
        return self.data

    def getNext(self):
        """ Returns the next node """
        return self.next

    def getDisplay(self):
        #TODO: Returns True if the letter stored in node should be displayed when
        #the Word Guess game prints the current game progress. Returns False otherwise.
        if self.display == True:
            return True
        else:
            return False

    def setData(self, newData):
        """ Sets newData as the element """
        self.data = newData

    def setNext(self, newNext):
        """ Sets newNext as the next node """
        self.next = newNext

    def setDisplay(self, newDisplay):
        #TODO: Sets whether or not the letter being stored in the node should
        #be displayed when the Word Guess game prints the current game progress.
        if newDisplay:
            self.display = True