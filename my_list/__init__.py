from ordering import Ordering

class MyList(Ordering):
    
    def __init__(self, _list=None):
        self.mapping_method = {
            'insertion': self.insertion,
            'merge': self.merge,
            'bubble': self.bubble
        }
        self._list = list(_list)

        # class 'Ordering' needs a copy of a given list
        self.copy(self._list)

    def __getitem__(self, index):
        return self._list[index]

    def __iter__(self):
        self.current_index = 0
        return self
    
    def __next__(self):

        if self.current_index < len(self._list) - 1:
            aux = self._list[self.current_index]
            self.current_index += 1
            return aux

        else:
            raise StopIteration

    def __repr__(self) -> str:
        return str(self._list)

    def sort(self, order='desc', method='insertion'):
        seleted_method = self.mapping_method.get(method)
        
        if seleted_method is not None:
            self._list = seleted_method(order=order, p=0, q=len(self._list))
            
        else:
            text = f"method '{method}' not exists. "
            text += 'possibilites are:'

            for item in self.mapping_method.keys():
                text += f'\n - {item}'

            text += '\n'

            assert False, text

    def append(self, element):
        self._list.append(element)
        self.copy(self._list)

    def remove(self, element):
        self._list.remove(element)
        self.copy(self._list)

    def indexOf(self, element):
        return self._list.indexOf(element)
    
    def pop(self, index):
        element = self._list.pop(index)
        self.copy(self._list)
        return element