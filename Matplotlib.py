import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
'''
散点图的绘画

'''
#创建一些数据
score = np.random.randint(0,100,(10,6))
score_df = pd.DataFrame(score) #数据结构
col = ["语文","数学","英语","物理","化学","体育"] #行索引序列
ide = ['同学'+str(i) for i in range(1,11)] #列索引
data = pd.DataFrame(score,columns=col,index=ide)
#创建一个画板进行作画
plt.figure(figsize=(20,20),dpi=100)
#获取你需要的数据
colors = ['red','gray','pink','blue','green','black','orange','purple','#ccc',"#33cccc"]
x = [i0 for i0 in range(1,11)]
y = [[],[],[],[],[],[]]
num = 0
for a in range(0,6):
    for b in range(0,10):
        y[a].append(score[b,a])

#绘图
for ele in range(0,6):

    plt.scatter(x,y[ele],s=100,c=colors[ele],marker='.')

plt.show()








