a = [1,2,3]
b = "adsfasfgdfhfdghgf"
b_list=[8,5,6,9,5,1]
#del a[1]
del(a[1])
print(a)
print(max(b))
print(min(b))
print(max(b_list))
print(min(b_list))
#只对字典的key排序
b_dict={"a":"3","b":"2","c":"1"}
print(max(b_dict))
print(min(b_dict))

print((1,1,1)<(2,2,2))
print([1,1,1]<[2,2,2])
#字典无法比较大小

print((1,2,3,4,5)[1:3])
print([1,2,3,4,5][1:3])
#字典无法进行切片

print([1,2]*5)
print((1,2)*5)
#字典不支持乘法

print("hello "+"python")
print((1,2)+(3,4))
print([1,2]+[3,4])
t_list=[1,2]
t_list.extend([3,4])
print(t_list)
t_list.append(0)
print(t_list)
t_list.append([5,6])
print(t_list)

print("a" in "abcdefg")
print("a" not in "abcdefg")
# in 在对 字典 操作时，判断的是 字典的键
print("a" in {"a":"b"})
print("b" in {"a":"b"})