#1-1
def TestUrl01(url,ReplaceStr):
    for i in range(0,len(url)):
        x=url[i:len(ReplaceStr)+i]
        if x=="tempId=-1":
            print("tempId=-1在第"+str(i)+"~"+str(len(ReplaceStr)+i)+"位")
            break
    url2=url[0:i]+"id=101"+url[(len(ReplaceStr)+i):]
    print("url2="+url2)
    return url2
def TestUrl02(url):
    ReplaceStr01="client="
    ReplaceStr02="q="
    for i in range(0,len(url)):
        x=url[i:len(ReplaceStr01)+i]
        y=url[i:len(ReplaceStr02)+i]
        z=url[i:i+1]
        if x=="client=":#7
            print("client=在第"+str(i)+"~"+str(len(ReplaceStr01)+i)+"位")
            for j1 in range(0,20,1):
                z1=url[len(ReplaceStr01)+i+j1:len(ReplaceStr01)+i+j1+1]
                if z1=="&":
                    print("client:"+url[len(ReplaceStr01)+i:len(ReplaceStr01)+i+j1])
        if y=="q=":#2
            print("q=在第"+str(i)+"~"+str(len(ReplaceStr02)+i)+"位")
            urlBehind=url[len(ReplaceStr02): ]
            for j2 in range(0,len(urlBehind),1):
                z2=url[len(ReplaceStr02)+i+j2:len(ReplaceStr02)+i+j2+1]
                if z2=="":
                    print("q="+url[len(ReplaceStr02)+i:len(ReplaceStr02)+i+j2])
                    break

def TestUrl03(url):
    dict = {'invitee': "John", 'event': "library", 'time': "Tomorrow 11 AM",'name': "Alex"};
    print(url.format(**dict))

