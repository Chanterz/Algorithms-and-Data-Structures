class List:
    def __init__(self, max_size):
        self.size = 0
        self.max_size = max_size
        self.values = [0 for _ in range(self.max_size)]
        self.removed_indices = [-1 for _ in range(self.max_size)]

    def insert(self, item, idx):
        if self.size == self.max_size or idx >= self.max_size:
            print("maximum count of elements reached")
        else:
            self.size += 1
            if len(self.removed_indices) == 0:
                self.values[idx] = item
            else:
                if idx in self.removed_indices:
                    self.values[idx] = item
                    self.removed_indices[idx] = -1
                else:
                    self.values[idx] = item

    def remove(self, idx):
        if self.values[idx] != " ":
            self.values[idx] = " "
            self.removed_indices[idx] = idx
            self.size -= 1

    def index(self, val):
        for idx, item in enumerate(self.values):
            if item == val:
                return idx

    def clear(self):
        self.values = []

    def print_list(self):
        for idx, value in enumerate(self.values):
            if idx not in self.removed_indices:
                print(value)


ls = List(10)

ls.insert("n", 0)
ls.insert("n", 2)
ls.insert("n", 6)
ls.insert("n", 8)
ls.insert("n", 3)

ls.print_list()
