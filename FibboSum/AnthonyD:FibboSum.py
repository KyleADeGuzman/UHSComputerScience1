
a=[]
b=[]
(x,y)=(1,2)
while x <= 4000000:
  b.append(x)
  b.append(y)
  x+=y
  y+=x
for i in b:
  if i % 2 ==0:
    a.append(i)
print(sum(a))
