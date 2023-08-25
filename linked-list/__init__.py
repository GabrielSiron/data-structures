from collections.abc import Iterable

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f"{self.value}"
    
class LinkedList:
    def __init__(self, elements: Iterable = None):
        if isinstance(elements, Iterable):
            self.head = Node(elements[0])
            aux = self.head
            for element in elements[1:]:
                aux.next = Node(element)
                aux = aux.next
        
        else:
            self.head = None

    def __iter__(self):
        self.aux = self.head
        return self

    def __next__(self):
        if self.aux:
            element = self.aux
            self.aux = self.aux.next
            return element 
        else:
            raise StopIteration
    
    def __len__(self):
        _list = list(enumerate(self))
        return len(_list)
    
    def __repr__(self):
        elements = [str(item.value) for item in self]
        list_repr = "[" + ", ".join(elements) + "]"

        return list_repr

    def __getitem__(self, wished_index) -> Node:
        for real_index, item in enumerate(self):
            if real_index == wished_index:
                return item
        else:
            raise IndexError

    def append(self, value) -> None:
        self.tail = self[len(self) - 1]
        self.tail.next = Node(value)

    def add_to_index(self, value=0, index=0) -> None:
        if index != 0:
            previous_element = self[index - 1]
            current_element = previous_element.next
            previous_element.next = Node(value)
            previous_element.next.next = current_element

        else:
            current_element = Node(value)
            current_element.next = self.head
            self.head = current_element

    def remove_in_index(self, index):
        lenght = len(self)

        if lenght == 0:
            raise IndexError
        
        if index != 0:
            previous_element = self[index - 1]
            element = previous_element.next

            if element.next:
                previous_element.next = element.next

            else:
                previous_element.next = None
        
        else:
            self.head = self.head.next

        pass


if __name__ == '__main__':
    lista = LinkedList([1, 2, 3, 4])
    print(lista)
    lista.remove_in_index(0)
    print(lista)
    lista.add_to_index(10, 2)
    print(lista)
    
    for x in lista:
        print(x)