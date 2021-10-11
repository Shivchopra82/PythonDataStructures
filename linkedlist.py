# CLASS NODE CREATES NEW NODE WHICH CONTAINS THE DATA AND THE LINK TO THE NEXT NODE 
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# CLASS LINKEDLIST CREATES THE LINKED LIST AND ASSIGN HEAD NODE
class LinkedList:
    def __init__(self):
        self.head = None


# PRINT FUNCTION WILL PRINT THE LINKED LIST
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            if itr.next: 
                llstr += str(itr.data)+' --> ' 
            else:
                llstr += str(itr.data)
            itr = itr.next
        print(llstr)


# GET LENGTH WILL SHOW THE LENGTH OF THE LINKED LIST
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count


# INSERT AT THE BEGINING WILL INSERT ELEMENTS AT THE BEGINING OF THE LINKED LIST 
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node



# INSERT AT THE END WILL INSERT ELEMENT AT THE END OF THE LINKED LIST
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)



#INSERT AT WILL INSERT THE GIVEN ELEMENT AT THE GIVEN INDEX OF THE LINKED LIST 
    def insert_at(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1


# REMOVE AT WILL REMOVE THE ELEMENT FROM THE GIVEN INDEX OF THE LINKED LIST
    def remove_at(self, index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count+=1


#INSERT AT WILL CREATE NEW LINKED LIST AND ADD ELEMENTS GIVEN IN THE INOPUT LIST
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    first = LinkedList()
    first.insert_values(["banana","mango","grapes","orange", "pineapple", "guava", "cherries"])
    first.insert_at(1,"cake")
    first.remove_at(2)
    first.remove_at(3)
    first.remove_at(4)
    first.print()

    first.insert_values([45,7,12,567,99,100,20,85,66,26,56,6,69])
    first.insert_at_end(67)
    first.print()


    new  = LinkedList()
    new.insert_at_begining(20)
    new.print()