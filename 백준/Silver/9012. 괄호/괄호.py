
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)

        if self.is_empty():  # 함수 사용
            self.top = new_node
        else:
            current = new_node
            current.next = self.top
            self.top = current

    def display(self):
        if self.is_empty():
            return

        current = self.top
        while current:
            print(f"|{current.data}|")
            current = current.next  # 한칸 아래로 이동

    def peek(self):
        if self.is_empty():
            return
            
        return self.top.data
        

    def pop(self):
        if self.is_empty():
            return
        
        temp = self.top.data
        self.top = self.top.next
        return temp
    


def is_checked(test):
    is_valid = True # 특정한 값을 찾을 수 없다면 boolean 하기

    #우리가 만든 stack 사용
    #여는 괄호가 있으면 스택에 넣고, 닫는 괄호가 나오면 pop
    vps = Stack()
    for ps in test:
        if ps == "(":
            vps.push(ps)
        else:
            if vps.pop() == "(":
                # for문 계속 실행
                continue # 반복문이 다음 회차 진행
            else:
                is_valid = False
                break

    # ((((( 나올 수 있어서 비어있어면 그대로
    if not vps.is_empty():
        is_valid = False        
        

    if is_valid:
        print("YES")
    else:
        print("NO")
        

num = int(input())
for _ in range(num):
    test = input()
    is_checked(test)