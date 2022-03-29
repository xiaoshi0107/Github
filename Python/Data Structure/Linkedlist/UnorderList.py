from Node import Node


class UnorderList():
    def __init__(self) -> None:
        self.head = None

    def isempty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.getnext()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.getnext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current != None:
            if current.getdata() != item:
                previous = current
                current = current.getnext()

            else:
                found = True
                if previous is None:
                    self.head = self.head.getnext()
                else:
                    previous.setnext(current.getnext())
        return found

    def check(self,):
        current = self.head
        while current != None:
            print(current.getdata())
            current = current.getnext()
    
    def append(self,data):
        current = self.head
        while current != None and current.getnext() !=None:
            current = current.getnext()
        current.setnext(Node(data))
    
    def pop(self):
        current = self.head
        while current.getnext().getnext() != None:
            current = current.getnext()
        current.setnext(None)


if __name__ == '__main__':
    print('start')
    mylist = UnorderList()
    mylist.add(10)
    mylist.add(11)
    mylist.add(12)
    mylist.add(13)
    mylist.add(14)
    mylist.add(15)
    mylist.add(16)
    mylist.add(17)
    mylist.add(18)
    mylist.check()
    mylist.pop()
    print('--------')
    mylist.check()