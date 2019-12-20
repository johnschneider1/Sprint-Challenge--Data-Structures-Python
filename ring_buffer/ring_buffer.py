from doubly_linked_list import DoublyLinkedList

# ring buffer is fixed size, when it fills up adding another element overwrites
# newest head, tail o


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check size to capacity
        if self.storage.length < self.capacity:
            # replace value of previous
            self.storage.add_to_head(item)
            # update current node is
            self.current = self.storage.tail
        else:
            self.current.value = item
            self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current_node = self.storage.tail

        while current_node:
            if current_node.value is not None:
                # add the current item
                list_buffer_contents.append(current_node.value)
            current_node = current_node.prev

        print(list_buffer_contents)

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
