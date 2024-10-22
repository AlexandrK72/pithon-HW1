n = int(input("Введите номер билета "))
res1 = 0
res2 = 0
m = 1
list_1 = []
k = 1
while k != 0:
        k = n//m
        remais = k%10
        list_1.append(remais)
        m *= 10
        k = n//m
l = (len(list_1))/2
for i in list_1[:int(l)]:
      res1 += i
for j in list_1[-int(l):]:
      res2 += j

if res1 == res2:
    print("yes")
else: print ("no")