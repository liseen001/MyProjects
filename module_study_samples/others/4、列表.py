#！/usr/bin/env python
# encoding: utf-8
# @author: Mrliu
# @file: demo.py
# @time: 2020/5/13 23:09
# @desc: 列表
s='hello'
print(list(s))
a=(1,2,3)
print(list(a))   #字符串、元祖强转为列表

numbers = [1,2,5,3,4,5,5,6,7,8]

#index 用于从列表中找出某个元素的位置\下标，如果有多个相同的元素，则返回第一个元素的位置,如果没有找到元素就会抛异常
print(numbers.index(5))

#count 用于统计某个元素出现在列表中的次数
print(numbers.count(55))

#append 用于在列表末尾添加新的元素
numbers =[1,2,3,5,7,8]
count=0
sum=0
for i in range(max(numbers)):
    count +=1
    sum +=count
    numbers.append(count)
    numbers.append(sum)
print(numbers)

#extend  讲一个新列表中的元素添加到原列表中，只能传列表
#append 和 extend可以接受一个列表作为参数，但是append方法是将其作为一个元素添加到列表中，而extend则是将列表的元素逐个添加到原列表中
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a,b)
a.extend([3])
print(a)

#  insert  将元素添加到下标值的位置
c =[1,2,3,4,5,6,7,8]
c.insert(max(c),20)
print(c)

# pop 移除列表中的一个元素，默认为最后一个，并且返回该元素的值  pop()  里面可以填列表下标，表示移除对应下标的值
d=[1,2,3,4,5]
print(d.pop(3))
print(d)

# remove 移除列表中匹配的值，如果多个匹配，则移除第一个
a=[1,2,3,4,5,3,4,50]
print(a.remove(3))
print(a)

# reverse  将列表中的元素进行反转
a=[1,2,3,4,5]
a.reverse()
print(a)

# sort 用于对列表进行排序，该方法会改变原来的列表，而不是返回新的排序列表，另外sort方法的返回值是空
a=[4,3,6,8,9,1]
b=a.sort()
print(b)   #返回值为空
print(a)  #原来的列表发生了改变

#sorted  不改变原列表，返回一个排序后的列表
a=[4,3,6,8,9,1]
b=sorted(a)
print(a)  #原列表没有改变
print(b)  #对源列表排序后的列表

#不管是sort还是sorted，默认的排序都是升序，如想要降序降序排序，需要制定排序参数，添加reverse参数
a=[1,2,3,4,3,6,5,7,9]
a.sort(reverse=True)
print(a)
a.sort(reverse=False)
print(a)

sorted(a,reverse=True)
print(a)