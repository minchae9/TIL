# 다시 보기
def enq(data):
    global qsize
    global rear
    global front
    if (rear+1)%qsize == front:     # 다시보기
        # print('Full')
        front = (front + 1) % qsize
    rear = (rear + 1) % qsize
    q[rear] = data

front = 0
rear = 0
qsize = 4
q = [0] * qsize
enq(1)
enq(2)
enq(3)
enq(4)
enq(5)  # 한 칸을 비워두므로 세 개 까지만 들어감
while front != rear:
    front = (front+1)%qsize
    