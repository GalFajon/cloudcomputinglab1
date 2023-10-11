import random
import time

for n in [30,50,80,100,150]:
    start = time.time()
    rows = n
    cols = n
    
    x = [ [ random.randint(0,20) for j in range(0,cols) ] for i in range(0,rows) ]
    y = [ [ random.randint(0,20) for j in range(0,cols) ] for i in range(0,rows) ]
    r = [ [ 0 for j in range(0,cols) ] for i in range(0,rows) ]
    
    for i in range(len(x)):
        for j in range(len(y[0])):
            for k in range(len(y)):
                r[i][j] += x[i][k] * y[k][j]
    
    end = time.time()
    print("Execution time for n=" + str(n) + " is: " + str(end - start))