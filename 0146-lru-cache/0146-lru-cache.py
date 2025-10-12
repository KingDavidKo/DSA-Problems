class LRUCache:

    def __init__(self, capacity: int):
        self.mydict = {}
        self.capacity = capacity
        self.size = 0
        self.first = None #Stores the key to the node
        self.last = None  #Stores the key to the node
    
    

    def get(self, key: int) -> int:
        if (key in self.mydict):
            value = self.mydict[key].val
            if self.mydict[key].prev is not None and self.mydict[key].next is not None:
                self.mydict[self.mydict[key].prev].next = self.mydict[key].next
                self.mydict[self.mydict[key].next].prev = self.mydict[key].prev

                self.mydict[self.first].prev = key
                self.mydict[key].prev = None
                self.mydict[key].next = self.first
                self.first = key
            elif self.mydict[key].prev is not None:
                self.mydict[self.mydict[key].prev].next = None
                self.last = self.mydict[key].prev

                self.mydict[self.first].prev = key
                self.mydict[key].prev = None
                self.mydict[key].next = self.first
                self.first = key
                
            elif self.mydict[key].next is not None:
                return value

            else:
                return value


            
            return value
           
        else:
            return -1

        

    def put(self, key: int, value: int) -> None:
     
        if key in self.mydict:
            self.mydict[key].val = value
            self.get(key)
            return
        
        if self.size < self.capacity:
            if self.size == 0:
                self.mydict[key] = Node(value)
                self.first = key
                self.last = key
                self.size = 1
            else:
                self.mydict[key] = Node(value)
                self.mydict[self.first].prev = key
                self.mydict[key].next = self.first
                self.first = key
                self.size += 1
        else:
            if (self.capacity > 1):
                secondLast = self.mydict[self.last].prev
                del self.mydict[self.last]
                self.last = secondLast
                self.mydict[secondLast].next = None
                self.size-=1
                self.put(key,value)
            else:
                del self.mydict[self.last]
                self.mydict[key] = Node(value)
                self.first = key
                self.last = key
                self.size = 1

            



class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)