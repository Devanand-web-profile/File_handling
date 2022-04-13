

data=open("myfile.txt","w")
data.write("hello robo  this is my robot")
data.flush()
print("data written")

#print(data.read())

x=data.read()
print(type(x))
print(data.read(10))
print(data.readline())
print(data.readlines())


count=0
for x in data.read(10):
    print(x,end=" ")

for x in data.read(10):
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        print("vowel is ", x)
        count=count+1
print(" total vowel :" , count)
