import numpy as np
m1 = np.arange(15).reshape(3,5)
m2 = np.arange(15,30).reshape(5,3)
m3 = np.dot(m1,m2)
print(np.dot(m1,m2))
rows,cols = m3.shape
for i in range(0,rows):
    for j in range(0,cols):
        if m3[i,j]>1000:
            m3[i,j] = m3[i,j]/2
        elif m3[i,j]<500:
            m3[i,j] *=2
for i in range(rows):
    for j in range(cols):
        m3[i,j] = m3[i,j]**2
print(np.sum(m3))


