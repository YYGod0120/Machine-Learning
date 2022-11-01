import pandas as pd
import numpy as np

#series
lst =[1,2,3,4,5,6]
index = [1,2,3,4,5,6]
ss = pd.Series(data=lst,index=index)
print(ss)
#Index和Values
print(ss.index)
print(ss.values)
#索引来获取数据
print(ss[5])


#DataFram
score = np.random.randint(0,100,(10,6))
score_df = pd.DataFrame(score) #数据结构
col = ["语文","数学","英语","物理","化学","体育"] #行索引序列
ide = ['同学'+str(i) for i in range(1,11)] #列索引

data = pd.DataFrame(score,columns=col,index=ide)
print(data)
print(data.T)

