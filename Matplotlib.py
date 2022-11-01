import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
score = np.random.randint(0,100,(10,6))
print(score)
score_df = pd.DataFrame(score) #数据结构
col = ["语文","数学","英语","物理","化学","体育"] #行索引序列
ide = ['同学'+str(i) for i in range(1,11)] #列索引

data = pd.DataFrame(score,columns=col,index=ide)
print(data)
x = [i0 for i0 in range(1,11)]
y = []
plt.figure(figsize=(20,20),dpi=100)
#创建画布等画图前提要素
for a in range(0,6):
    for b in range(0,10):
        y.append(score[b,a])

    print(y)


