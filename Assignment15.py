q1>def find_next_greater(arr):
    stack = []
    output = [-1] * len(arr)

    for i in range(len(arr)-1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            output[i] = stack[-1]

        stack.append(arr[i])

    return output

q2>def find_nearest_smaller(arr):
    stack = []
    output = [-1] * len(arr)

    for i in range(len(arr)):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            output[i] = stack[-1]

        stack.append(arr[i])

    return output


q3>class Stack:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, element):
        self.q1.append(element)

    def pop(self):
        if not self.q1 and not self.q2:
            raise IndexError("Stack is empty")

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        return self.q1.pop()

    def top(self):
        if not self.q1 and not self.q2:
            raise IndexError("Stack is empty")

        while len(self.q1) > 1:
            self.q2.append(self.q1.pop(0))

        top_element = self.q1[0]
        self.q2.append(self.q1.pop())

        self.q1, self.q2 = self.q2, self.q1  # Swap q1 and q2

        return top_element


q4>def reverse_stack(stack):
    if len(stack) <= 1:
        return

    temp = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, temp)


def insert_at_bottom(stack, item):
    if len(stack) == 0:
        stack.append(item)
        return

    temp = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(temp)
q5>def reverse_string(S):
    stack = []
    for char in S:
        stack.append(char)

    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    return reversed_string


q6>def evaluate_postfix(S):
    stack = []

    for char in S:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2

            stack.append(result)

    return stack.pop()

q7>class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, element):
        self.main_stack.append(element)

        if not self.min_stack or element <= self.min_stack[-1]:
            self.min_stack.append(element)

    def pop(self):
        if self.main_stack:
            popped = self.main_stack.pop()

            if popped == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self):
        if self.main_stack:
            return self.main_stack[-1]

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]

q8>def trap_water(heights):
    left = 0
    right = len(heights) - 1
    left_max = right_max = total_water = 0

    while left <= right:
        if heights[left] <= heights[right]:
            left_max = max(left_max, heights[left])
            water_level = left_max - heights[left]
            total_water += water_level
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water_level = right_max - heights[right]
            total_water += water_level
            right -= 1

    return total_water
