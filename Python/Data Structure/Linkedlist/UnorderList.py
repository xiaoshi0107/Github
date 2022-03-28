from Node import Node

class UnorderList():
    def __init__(self) -> None:
        self.head = None

    def isempty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setnext(self.head)
        self.head = temp

if __name__ == '__main__':
    mylist = UnorderList()
    mylist.add(10)