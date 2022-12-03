class HashTable:

    def __init__(self, size):
        self.size = size
        self.table = [{} for _ in range(size)]

    def hash(self, input):
        #input type: int or string
        #return type: int
        slot = hash(input) % (self.size)
        return slot

    def insert(self, input):
        #input type: int or string
        #return type: none
        slot = self.hash(input)
        if input not in self.table[slot]:
            self.table[slot][input] = None
        return None

    def search(self, input):
        #input type: int or string
        #return type: boolean
        slot = self.hash(input)
        if input in self.table[slot]:
            return True
        return False

    def remove(self, input):
        #input type: int or string
        #return type: none
        slot = self.hash(input)
        if input in self.table[slot]:
            del self.table[slot][input]
        else:
            print(f'Item {input} not found')
        return None

    def print(self):
        #input type: none
        #return type: none
        for i in range(self.size):
            print(list(self.table[i].keys()))
        return None


if __name__ == "__main__":
    HT = HashTable(10000)
    lista = []
    sum = 0
    words1 = open('words_alpha.txt', encoding='utf-8')
    words2 = open('kaikkisanat.txt', encoding='utf-8')
    for key in words1:
        lista.append(key.strip('\n'))
    for key2 in words2:
        if key2.strip('\n') in lista:
            sum += 1
    print(sum)