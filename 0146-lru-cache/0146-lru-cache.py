class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.nodeMap = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        nextNode = self.head.next
        nextNode.prev = node
        self.head.next = node
        
        self.nodeMap[node.key] = node
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        
        del self.nodeMap[node.key]

    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        
        value = self.nodeMap[key].value
        self.removeNode(self.nodeMap[key])
        self.addNode(Node(key, value))
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.nodeMap:
            self.removeNode(self.nodeMap[key])
        
        newNode = Node(key, value)
        self.addNode(newNode)
        
        if len(self.nodeMap) > self.capacity:
            self.removeNode(self.tail.prev)
        
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)