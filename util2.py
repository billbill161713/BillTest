import json,sys
#1
def Test0214_3(json1,json2,number):
    label=[]
    if number>4:
        print("excessive")
        sys.exit()
    else:
        for s in range(0,number):
            label.append(input("input:"))
    box=[]
    box2=[]
    box3=[]
    box4=[]
    i=0
    with open(json2, 'r') as f2:
        data2 = json.load(f2)
    with open(json1, 'r') as f:
        data = json.load(f)
    for item in data:
        box.append(item['title'])
        box2.append(item['category'])
        box3.append(item['tag'])
        box4.append(item['completed'])
    for item2 in data2:
        box.append(item2['title'])
        box2.append(item2['category'])
        box3.append(item2['tag'])
        box4.append(item2['completed'])
  
    x=sorted(box)#
    for i in range(0,len(box)):
        for z in range(0,int(number)):
            if label[z] =='title':
                print('title:'+x[i])
            if label[z] =='category':
                print("category:"+box2[box.index(x[i])])
            if label[z] =='tag':
                print("tag:"+box3[box.index(x[i])])
            if label[z] =='completed':
                print("completed:"+box4[box.index(x[i])]+"\n")
                    
                    
def Test0214_2(json_3):
    box=[]
    box2=[]
    parentX1=[]
    parentX2=[]
    parentX3_1=[]
    with open(json_3, 'r') as f:
        data = json.load(f)
    for item in data:
        box.append(item['title'])
        box2.append(item['parent'])
    for i in range(0,len(box2)):
        parentX2.append(box2[i])
        parentX3_1.append(box2[i])
        parentX3_1.append(box[i])
        parentX3_1.append(" ")
    print(parentX2)
        
        
        
            

        
            
 

    
                        



print("#1")
Test0214_3('todo-1.json','todo-2.json',4)

#Test0214_2('todo-3.json')
print("#3")
Test0214_3('todo-1.json','todo-2.json',1)
