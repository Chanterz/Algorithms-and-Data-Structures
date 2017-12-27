from lab.linkedList import List


class Stack:
    def __init__(self):
        self.values = List()

    def push(self, item):
        self.values.append(item)

    def pop(self):
        return self.values.pop()

    def top(self):
        return self.values.end.val

    def clear(self):
        self.values.clear()

    def is_empty(self):
        return self.values.root is None

st = Stack()

print(st.is_empty())
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
print(st.is_empty())
print(st.top())
print(st.pop())
print(st.top())
