import random
list1=[2,5,6,7]
list2=[1,4,5,7]
list3=[2,3,6,7]
list4=[1,3,5,6]
list5=[1,2,4,5]

for t in range(1,5):

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

    file = open('day3.txt', 'w')
    file.write(str(res1)+'\n')
    file.write(str(res2)+'\n')
    file.write(str(res3)+'\n')
    file.write(str(res4)+'\n')
    file.write(str(res5)+'\n')

    file.close()

