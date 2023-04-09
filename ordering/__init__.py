class Ordering:

    def __init__(self):
        pass
        
    def copy(self, _list):
        self._list = list(_list)

    def insertion(self, order: str ='desc', **kwargs):
        for j in range(1, len(self._list)):
            key = self._list[j]
            i = j - 1
            
            # ascending
            while i >= 0 and self._list[i] > key and order == 'asc':
                self._list[i + 1] = self._list[i] 
                i -= 1

            # descending
            while i >= 0 and self._list[i] < key and order == 'desc':
                self._list[i + 1] = self._list[i] 
                i -= 1

            self._list[i + 1] = key
        
        return self._list

    def merge(self, p: int = 0, q: int = 0, order: str ='desc', **kwargs):

        if abs(p - q) == 1:
            return [self._list[p]]

        middle_index = int((abs(p + q))/2)

        first = self.merge(p, middle_index, order=order)
        second = self.merge(middle_index, q, order=order)

        i = j = 0

        limit_first = len(first)
        limit_second = len(second)

        ordened_list = []

        while i < limit_first and j < limit_second:
            
            if order == 'asc':
                if first[i] < second[j]:
                    ordened_list.append(first[i])
                    i += 1
                else:
                    ordened_list.append(second[j])
                    j += 1
            else:
                if first[i] > second[j]:
                    ordened_list.append(first[i])
                    i += 1
                else:
                    ordened_list.append(second[j])
                    j += 1

        if j == limit_second:
            ordened_list.extend(first[i:])
        
        else:
            ordened_list.extend(second[j:])

        if len(ordened_list) == len(self._list):
            self._list = ordened_list

        return ordened_list

    def bubble(self, order='asc', **kwargs):
        for x in range(len(self._list)):
            for y in range(x + 1, len(self._list)):

                # ascending
                if self._list[x] < self._list[y]:
                    self.exchange(x, y)

                # descending
                if self._list[x] > self._list[y]:
                    self.exchange(x, y)
        
        return self._list

    def exchange(self, x, y):
        aux = self._list[x]
        self._list[x] = self._list[y]
        self._list[y] = aux