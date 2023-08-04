# Answer 1
list1=[]
list2=[]
i=int(input("press 1 for enter list or 0 for exits"))
v=0
while(v>=0):
    if(i==1):
        val=input("Enter value")
        list1[i].append(val)
        v+=1
    else:
        v=-1
for i in range(0,len(list1)):
    val2=input("Enter the value: ")
    list2[i].append(val2)

dict={}
for i in range(0,len(list1)):
    dict[list1[i]] = list2[i]
print(dict)