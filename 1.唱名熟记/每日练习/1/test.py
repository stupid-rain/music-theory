import random
list1=[1,4,5]
list2=[2,3,6]
list3=[4,6,7]
list4=[1,2,6]
list5=[3,5,7]


res1 = []
for i in range(1,100):
    res1.append(random.choice(list1))

res2 = []
for i in range(1,100):
    res2.append(random.choice(list2))

res3 = []
for i in range(1,100):
    res3.append(random.choice(list3))

res4 = []
for i in range(1,100):
    res4.append(random.choice(list4))

res5 = []
for i in range(1,100):
    res5.append(random.choice(list5))


file = open('day1.txt', 'w')
file.write(str(res1)+'\n')
file.write(str(res2)+'\n')
file.write(str(res3)+'\n')
file.write(str(res4)+'\n')
file.write(str(res5)+'\n')

file.close()
