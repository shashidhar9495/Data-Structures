### Multithreading with que

from collections import deque
import threading
import time

orders=['pizza','samosa','pasta','biriyani','burger']
requests=deque()
def take_order(orders):
    
    global requests
    for order in orders:
        requests.appendleft(order)
        print('you ordered:{}'.format(order))
        time.sleep(0.5)
    

def serve_orders(orders):
    for order in orders:
        time.sleep(2)
        print('you are served with:{}'.format(requests.pop()))
        
            
t1=threading.Thread(target=take_order,args=(orders,))
t2=threading.Thread(target=serve_orders,args=(orders,))

t1.start()
time.sleep(1)
t2.start()

t1.join()
t2.join()