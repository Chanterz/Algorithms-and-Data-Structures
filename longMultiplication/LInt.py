base = 10e9
first_num = [123, 456, 789]
second_num = [123, 456, 789]


def add(left, right):
    carry = 0
    for i in range(max(len(left), len(right)) or carry):
        if i == len(left):
            left.append(0)
        left[i] += carry + (right[i] if i < len(left) else 0)
        carry = left[i] >= base
        if carry:
            left[i] -= base


add(first_num, second_num);

print(first_num)
