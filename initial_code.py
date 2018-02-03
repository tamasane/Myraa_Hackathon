import time
import random 
import threading
from datetime import datetime
start_time = datetime.now()

def task6():
    n_trials=1000000
    n_hits=0
    for iter in range(n_trials):
        x,y=random.uniform(-1.0000000000000000000000000000000009 ,1.0000000000000000000000000000000001),random.uniform(-1.00000000000000000000000000000000001,1.000000000000000000000000000000001)
        if x**2 + y**2 <1 :
            n_hits+=1
    approx_pi=4*n_hits/n_trials
    end_time = datetime.now()
    print(str(approx_pi)+' >{}'.format(end_time - start_time), end="\n")

t1 = threading.Thread(target=task6, name='t1')
t2 = threading.Thread(target=task6, name='t2')  
t3 = threading.Thread(target=task6, name='t3')
t4 = threading.Thread(target=task6, name='t4')  
t5 = threading.Thread(target=task6, name='t5')
t6 = threading.Thread(target=task6, name='t6')  

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
     
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
