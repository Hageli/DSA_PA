##################################################
# kurssi: BM40A1500 Data Structures and Algorithms
# opiskelija: 0604373, Miro Hagelberg
# päivämäärä: 3.12.2022
##################################################

class Node:

    def __init__(self, key, next):
        self.key = key
        self.next = next

class LinkedList:

    def __init__(self):
        self.length = 0
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)

    def insert(self, input):
        #input type: int or string
        #return type: none
        current = self.head
        while current.next.key != None:
            current = current.next
        current.next = Node(input, self.tail)
        self.length += 1
        return None
        
    def remove(self, input):
        #input type: int or string
        #return type: boolean
        position = self.findIndex(input)
        if position == -1:
            return False
        current = self.head
        for i in range(position):
            current = current.next
        current.key = current.next.key
        if(current.next == self.tail):
            self.tail = current
        current.next = current.next.next
        self.length -= 1
        return True


    def findIndex(self, data):
        #input type: int or string
        #return type: int
        current = self.head
        counter = 0
        while current.next != None:
            if current.key == data:
                return counter
            else:
                counter += 1
                current = current.next
        return -1

    def search(self, input):
        #input type: int or string
        #return type: boolean
        current = self.head.next
        while current.next != None:
            if current.key == input:
                return True
            current = current.next
        return False


    def print(self):
        #input type: none
        #return type: none
        current = self.head.next
        print('[', end='')
        while current.next != None:
            print(current.key, end='')
            current = current.next
            if current.key != None:
                print(', ', end='')
        print(']')
        return None



class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [LinkedList() for _ in range(size)]

    def hash(self, input):
        #input type: int or string
        #return type: int
        slot = hash(input) % (self.size)
        return slot

    def insert(self, input):
        #input type: int or string
        #return type: none
        index = self.hash(input)
        self.table[index].insert(input)
        return None

    def search(self, input):
        #input type: int or string
        #return type: boolean
        index = self.hash(input)
        return self.table[index].search(input)

    def remove(self, input):
        #input type: int or string
        #return type: none
        index = self.hash(input)
        self.table[index].remove(input)
        return None

    def print(self):
        #input type: none
        #return type: none
        for i in range(self.size):
            self.table[i].print()
        return None


if __name__ == "__main__":
    HT = HashTable(10000)
    sum = 0
    words1 = open('words_alpha.txt', encoding='utf-8')
    for key in words1:
        HT.insert(key.strip('\n'))

    words2 = open('kaikkisanat.txt', encoding='utf-8')
    for key2 in words2:
        if HT.search(key2.strip('\n')):
            sum += 1

    print(sum)