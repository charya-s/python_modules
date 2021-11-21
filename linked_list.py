class Node():
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
class LList():
    def __init__(self):
        self.head = None

    def insert_at_start(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def create_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        if index is 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count is index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, data, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index.")
        if index is 0:
            self.insert_at_start(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count is index-1:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next
            count += 1

    def remove(self, value):
        itr = self.head
        found = False
        if itr.data is value:
            self.head = itr.next
            found = True
        while itr:
            if (itr.next is not None) and (itr.next.data is value):
                itr.next = itr.next.next
                found = True
            itr = itr.next
        if not found:
            print("No such value in list.")

    def insert_after(self, value, data):
        itr = self.head
        found = False
        while itr:   
            if itr.data is value:
                itr.next = Node(data, itr.next)
                found = True
            itr = itr.next
        if not found:
            print("No such value in list.")


    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("List is empty")
            return 0
        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        
        print(llstr)