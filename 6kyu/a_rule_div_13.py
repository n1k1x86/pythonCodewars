import queue

q = queue.Queue(maxsize=6)

def queue_clear():
    global q
    while not q.empty():
        q.get(block=False)

def queue_create():
    global q
    q_elem = [1, 10, 9, 12, 3, 4]
    for i in q_elem:
        q.put(i)

def get_new_num(el):
    global q
    el = int(el)
    q_el = q.get()
    q.put(q_el)
    return el * q_el
    
def thirt(n):
    global q
    queue_create()
    new_num = 0
    prev_num = n
    running = True
    while running:
        new_num = sum(list(map(get_new_num, str(prev_num)[::-1])))
        queue_clear()
        queue_create()
        if prev_num == new_num:
            running = False
        prev_num = new_num
    return new_num
