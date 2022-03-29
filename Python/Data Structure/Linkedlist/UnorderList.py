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


if __name__ == '__main__':
    print('start')
    mylist = UnorderList()
    mylist.add(10)
    print(mylist.search(10))