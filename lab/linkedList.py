class Node:
    def __init__(self, val, nxt=None):
        self.nxt = nxt
        self.val = val


class List:
    def __init__(self, root_val=None):
        if root_val is not None:
            self.end = self.root = Node(root_val)
        else:
            self.end = self.root = None
        self.current = self.root
        self.len = 0

    def __str__(self):
        if self.len:
            rt = self.root
            rslt = ''
            while rt is not None:
                rslt += rt.val + (" -> " if rt.nxt is not None else "")
                rt = rt.nxt
            return rslt
        return ""

    def __iter__(self):
        self.current = self.root
        return self

    def __next__(self):
        if self.current is not None:
            val_to_return = self.current
            self.current = self.current.nxt
            return val_to_return
        else:
            raise StopIteration

    def __getitem__(self, item):
        for idx, i in enumerate(self):
            if idx == item:
                return i

    def append(self, new_val):
        if self.root is not None:
            self.end.nxt = Node(new_val)
            self.end = self.end.nxt
            self.len += 1
        else:
            self.root = self.end = Node(new_val)

    def delete(self, val):
        prev = None

        for i in self:
            if i.val == val and i is not self.root and i is not self.end:
                prev.nxt = i.nxt
                del i
                self.len -= 1
                return True

            elif i.val == val and i is self.root:
                self.root = self.root.nxt
                self.len -= 1
                return True

            elif i.val == val and i is self.end:
                prev.nxt = None
                self.end = prev
                self.len -= 1
                return True
            prev = i
        return False

    def pop(self):
        prev = None

        for i in self:
            if i is self.end:
                return_value = self.end.val
                self.end = prev
                return return_value
            prev = i

    def insert(self, val, index=None, index_val=None):
        if index >= self.len:
            raise IndexError
        if index is not None:
            if index == 0:
                self.len += 1
                self.root = Node(val, self.root)
                return True
            prev = None
            for idx, i in enumerate(self):
                if idx == index - 1:
                    prev.nxt = Node(val, i)
                    self.len += 1
                    return True

        elif index_val is not None:
            for i in self:
                if i.val == index_val:
                    i.nxt = Node(val, i.nxt)
                    self.len += 1
                    return True
        return False

    def index(self, val):
        for idx, i in enumerate(self):
            if i.val == val:
                return idx
        raise IndexError

    def clear(self):
        self.__init__(None)
