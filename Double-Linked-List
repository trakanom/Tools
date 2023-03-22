class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self, value=None):
        self.value = value
        if self.value is not None:
            self.head = Node(self.value)
            self.tail = self.head
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0

    def add_to_head(self, val):
        print(f"Adding {val} to head")
        if self.head is None:
            self.head = Node(val)
            self.length += 1
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head
            self.length += 1

    def add_to_tail(self, val):
        print(f"Adding {val} to tail")
        if self.tail is None:
            self.tail = Node(val)
            self.length += 1
        else:
            new_tail = Node(val)
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail
            self.length += 1

    def get_index(self, value):
        return self.traverse("Index", value)

    def get_value(self, index):
        return self.traverse("Value", index)

    def get_node(self, value):
        return self.traverse("Node", value)

    def contents(self):
        return self.traverse("contents")

    def contains(self, value):
        return self.get_index(value) is not None

    def pop(self, value):
        print(f"Popping {value} from list.")
        node = self.get_node(value)
        if node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next
            node.next.prev = None
        else:
            node.prev.next = node.next

        self.length -= 1

    def traverse(self, query_type, value=None):
        index = 0
        current_node = self.head

        if query_type.lower() == "index":
            result = None

        if query_type.lower() == "value":
            result = None

        if query_type.lower() == "contents":
            contents = "["

        while current_node is not None:
            if query_type.lower() == "contents":
                contents += f"'{current_node.value}', "

            if query_type.lower() == "value":
                if index == value:
                    result = current_node.value
                    break

            elif query_type.lower() == "index" or query_type.lower() == "node":
                if current_node.value == value:
                    result = index if query_type.lower() == "index" else current_node
                    break

            current_node = current_node.next
            index += 1

        if query_type.lower() == "contents":
            contents = contents[:-2] + "]"
            return contents

        return result


car = LinkedList()
car.add_to_head("subaru")
car.add_to_head("ford")
car.add_to_tail("tesla")
print(car.length)

check_var = "Nixon"
print(f"Car.contains('{check_var}') == {car.contains(check_var)}")
print(car.length)
