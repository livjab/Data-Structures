from doubly_linked_list import DoublyLinkedList

class LRUCache:
    def __init__(self, limit=10):
        self.limit = limit
        self.current_size = 0
        self.storage = DoublyLinkedList()
        self.dict = {}

    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.storage.move_to_front(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        if key in self.dict:
            node = self.dict[key]
            node.value = (key, value)
            self.storage.move_to_front(node)
            return

        if self.current_size == self.limit:
            del self.dict[self.storage.tail.value[0]]
            self.storage.remove_from_tail()
            self.current_size -= 1

        self.storage.add_to_head((key, value))
        self.dict[key] = self.storage.head
        self.current_size += 1
