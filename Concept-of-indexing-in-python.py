#task
x=[1,2,3,4,5]
y=[11,12,13,14,15]
print("--(a)--")
for i in range(len(x)):   
    print(3*x[i])
print("--(b)--")
for i in range(len(x)):
    for j in range(len(y)):
        print(x[i]+y[j])
print("--(c)--")
for i in range(len(x)):
    for j in range(len(y)):
        print(x[i]-y[j])
print("--(d)--")
print("Value of x[1] is :",x[1])
print("--(e)--")
print("Value of x[0] is:",x[0])
print("--(f)--")
print("Value of x[-1] is :",x[-1])
print("--(g)--")
print("Value of x[:] is: ",x[:])
print("--(h)--")
print("The value of x[2:4] is:",x[2:4])
print("--(i)--")
print("The value of x[1:4:2] is:",x[1:4:2])
print("--(j)--")
print("The value of x[:2] is:",x[:2])
print("--(k)--")
print("The value of x[::2] is:",x[::2])

        

