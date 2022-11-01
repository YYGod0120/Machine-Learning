import numpy as np

#array的创建
# ndmin用于指定生成数组的最小维度
a = np.array([[1,2,3],[4,5,6]],ndmin=3)
print(a)
'''
ndarray的属性
.shape 数组维度的元组
.ndim数组维度
.size元素数量
.itemsize数组长度（字节）
.dtype 数组元素的类型
'''

#生成0和1的数组
ones = np.ones([1,8])  #[行,列]
print(ones)
zeros = np.zeros([1,8])
print(zeros)
#.empty()创建指定形状,类型且未初始化的数组,存的是之前内存的值
b = np.empty([3,8],dtype=int)
print(b)

c = np.array([[1,2,3],[4,5,6]])
# 从现有的数组当中创建
c1 = np.array(c)  #内存中创建一个新的对象
# 相当于索引的形式，并没有真正的创建一个新的
c2 = np.asarray(c) #指针指向c
