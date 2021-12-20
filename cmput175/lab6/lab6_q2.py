class BoundedQueue:
    # Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        assert isinstance(capacity, int), 'Error: Type error: %s' % (type(capacity))
        assert capacity >= 0, 'Error: Illegal capacity: %d' % (capacity)
        self.__items = []
        self.__capacity = capacity
    
    # Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        if len(self.__items) >= self.__capacity:
            raise Exception('Error: Queue is full')
        self.__items.append(item)
    
    # Removes and returns the front-most item in the queue. # Returns nothing if the queue is empty.
    def dequeue(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items.pop(0)
    
    # Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        if len(self.__items) <= 0:
            raise Exception('Error: Queue is empty')
        return self.__items[0]
    
    # Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        return len(self.__items) == 0
    
    # Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return len(self.__items) == self.__capacity
    
    # Returns the number of items in the queue:
    def size(self):
        return len(self.__items)
    
    # Returns the capacity of the queue:
    def capacity(self):
        return self.__capacity
    
    # Removes all items from the queue, and sets the size to 0 # clear() should not change the capacity
    def clear(self):
        self.__items = []
    
    # Returns a string representation of the queue:
    def __str__(self):
        str_exp = "]"
        for item in self.__items:
            str_exp += (str(item) + ",")
        str_exp = list(str_exp)
        if str_exp[-1] == ",":
            str_exp[-1] = ""
        str_exp = "".join(str_exp)
        return str_exp + "]"


class CircularQueue:
    # Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity <= 0:
            raise Exception ("Capacity Error")
        self.__items = []
        self.__capacity = capacity
        self.__count = 0
        self.__head = 0
        self.__tail = 0

    # Adds a new item to the back of the queue, and returns nothing
    def enqueue(self, item):
        if self.__count == self.__capacity:
            raise Exception('Error: Queue is full')
        if len(self.__items) < self.__capacity:
            self.__items.append(item)
        else:
            self.__items[self.__tail] = item
        self.__count += 1
        self.__tail = (self.__tail +1) % self.__capacity
    
    # Removes and returns the front-most item in the queue. # Returns nothing if the queue is empty.
    def dequeue(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        item = self.__items[self.__head]
        self.__items[self.__head] = None
        self.__count -= 1
        self.__head=(self.__head+1) % self.__capacity
        return item
    
    # Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        if self.__count == 0:
            raise Exception('Error: Queue is empty')
        return self.__items[self.__head]
    
    # Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        return self.__count == 0
    
    # Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return self.__count == self.__capacity
    
    # Returns the number of items in the queue:
    def size(self):
        return self.__count
    
    # Returns the capacity of the queue:
    def capacity(self):
        return self.__capacity
    
    # Removes all items from the queue, and sets the size to 0 # clear() should not change the capacity
    def clear(self):
        self.__items = []
        self.__count = 0
        self.__head = 0
        self.__tail = 0
    
    # Returns a string representation of the queue:
    def __str__(self):
        str_exp = "]"
        i=self.__head
        for j in range(self.__count):
            str_exp += str(self.__items[i]) + ","
            i=(i+1) % self.__capacity
        str_exp = list(str_exp)
        if str_exp[-1] == ",":
            str_exp[-1] = ""
        str_exp = ''.join(str_exp)
        return str_exp  + "]"


# Use BondedQueue to complete the task
def BoundedQueue_Test():
    normal_customers = BoundedQueue(3)
    VIP_customers = BoundedQueue(3)
    
    while True:
        # Continues asking which operations user want to do
        operation = input("Add, Serve, or Exit: ")
        if operation == "Add":
            add_name = input("Enter the name of the person to add: ")
            isVIP = input("Is the customer VIP? ")
            if isVIP == "True":
                # if the customer is VIP and the VIP customer queue is not full
                if VIP_customers.isFull() == False:
                    VIP_customers.enqueue(add_name)
                    print("Add %s to VIP line" %(add_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
                else:
                    print("Error: VIP customers queue is full")
            elif isVIP == "False":
                # if the customer is not VIp and the normal customer queue is not full
                if normal_customers.isFull() == False:
                    normal_customers.enqueue(add_name)
                    print("Add %s to the normal line." %(add_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
                else:
                    print("Error: Normal customers queue is full")
        
        elif operation == "Serve":
            # if both VIP customer queue and normal customer queue is empty
            if VIP_customers.isEmpty() == True and normal_customers.isEmpty() == True:
                print("Error: Queues are empty")
            else:
                if VIP_customers.isEmpty() == False:
                    serve_name = VIP_customers.dequeue()
                    print("%s has been served" %(serve_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
                elif VIP_customers.isEmpty() == True:
                    serve_name = normal_customers.dequeue()
                    print("%s has been served" %(serve_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
        
        elif operation == "Exit":
            print("Quitting")
            break


def CircularQueue_Test():
    normal_customers = CircularQueue(3)
    VIP_customers = CircularQueue(3)
    
    while True:
        # Continues asking which operations user want to do
        operation = input("Add, Serve, or Exit: ")
        if operation == "Add":
            add_name = input("Enter the name of the person to add: ")
            isVIP = input("Is the customer VIP? ")
            if isVIP == "True":
                # if the customer is VIP and the VIP customer queue is not full
                if VIP_customers.isFull() == False:
                    VIP_customers.enqueue(add_name)
                    print("Add %s to VIP line" %(add_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
                else:
                    print("Error: VIP customers queue is full")
            elif isVIP == "False":
                # if the customer is not VIp and the normal customer queue is not full
                if normal_customers.isFull() == False:
                    normal_customers.enqueue(add_name)
                    print("Add %s to the normal line." %(add_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
                else:
                    print("Error: Normal customers queue is full")
        
        elif operation == "Serve":
            # if both VIP customer queue and normal customer queue is empty
            if VIP_customers.isEmpty() == True and normal_customers.isEmpty() == True:
                print("Error: Queues are empty")
            else:
                if VIP_customers.isEmpty() == False:
                    serve_name = VIP_customers.dequeue()
                    print("%s has been served" %(serve_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
                elif VIP_customers.isEmpty() == True:
                    serve_name = normal_customers.dequeue()
                    print("%s has been served" %(serve_name))
                    print("Normal customers queue: ", normal_customers)
                    print("VIP customers queue: ", VIP_customers)
        
        elif operation == "Exit":
            print("Quitting")
            break

BoundedQueue_Test()
#CircularQueue_Test()