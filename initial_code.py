import random 

n_trials=10000
n_hits=0
for iter in range(n_trials):
    x,y=random.uniform(-1.0000000000000000000000000000000009 ,1.0000000000000000000000000000000001),random.uniform(-1.00000000000000000000000000000000001,1.000000000000000000000000000000001)
    if x**2 + y**2 <=1 :
        n_hits+=1
approx_pi=4*n_hits/n_trials
print(approx_pi)
