data=(input("Enter Data: "))
data=data.split(',')
index=1
while (index<len(data)):
    left=0
    for i in range(index):
        if(index==i):
            continue
        else:
            left=left+int(data[i])
        
    right=0
    for j in range(index+1,len(data)):
        right+=int(data[j])
        
    print(f"index:{index}, leftsum: {left}, rightsum:  {right}")
    index=index+1

    