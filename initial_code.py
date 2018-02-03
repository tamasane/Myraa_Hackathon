n_trials=100000
n_hits=0
points = set()
x,y=random.uniform(-1.0000000000000000000001,1.000000000000000000000001),random.uniform(-1.000000000000000000000000001,1.0000000000000000000000000001)
for iter in range(n_trials):
    while (x,y) in points:
        x,y=random.uniform(-1.0000000000000000000001,1.000000000000000000000001),random.uniform(-1.000000000000000000000000001,1.0000000000000000000000000001)
    points.add((x,y))
    if x**2 + y**2 <1 :
       n_hits+=1
approx_pi=4*n_hits/n_trials
