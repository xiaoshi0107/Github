from sympy import preview
from Node import Node


class OrderList():
    def __init__(self) -> None:
        self.head = None

    def isempty(self):
        return self.head == None

    def printlist(self,):
        current = self.head
        while current != None:
            print(current.getdata())
            current = current.getnext()

    def add(self, item):
        found = False
        temp = Node(item)
        previous = None
        current = self.head
        # 空列表
        if self.head == None:
            self.head = temp
        # 加到开头
        elif item <= current.getdata():
            temp.setnext(current)
            self.head = temp
        # 不是开头
        else:
            while current != None and found == False:
                if item <= current.getdata():
                    previous.setnext(temp)
                    temp.setnext(current)
                    found = True

                elif current.getnext() == None:
                    current.setnext(temp)
                    found = True

                else:
                    previous = current
                    current = current.getnext()
    
    def remove(self,item):
        current = self.head
        found = False
        previous = None
        if item == self.head.getdata():
            self.head = self.head.getnext()
        else:
            while item != current.getdata():
                previous = current
                current = current.getnext()
            previous.setnext(current.getnext())
                



if __name__ == '__main__':
    mylist = OrderList()
    mylist.printlist()
    mylist.add(10)
    mylist.add(15)
    mylist.add(14)
    mylist.add(17)
    mylist.add(11)
    mylist.add(1)
    mylist.add(12)
    mylist.add(10)
    mylist.add(110)
    mylist.printlist()
    mylist.remove(10)
    mylist.printlist()
