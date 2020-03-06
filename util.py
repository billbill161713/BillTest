#1-1
def replaceString(url, oldPattern, newPattern):
    for i in range(0,len(url)):
        x=url[i:len(oldPattern)+i]
        if x==oldPattern:
            #print("tempId=-1在第"+str(i)+"~"+str(len(ReplaceStr)+i)+"位")
            break
    url2=url[0:i]+newPattern+url[(len(oldPattern)+i):]
    print("url2="+url2)
    return url2


def queryParameter(url,ReplaceStr01,ReplaceStr02):
    for i in range(0,len(url)):
        x=url[i:len(ReplaceStr01)+i]
        y=url[i:len(ReplaceStr02)+i]
        if x=="client=":#7
            #print("client=在第"+str(i)+"~"+str(len(ReplaceStr01)+i)+"位")
            for j1 in range(0,20,1):
                z1=url[len(ReplaceStr01)+i+j1:len(ReplaceStr01)+i+j1+1]
                if z1=="&":
                    print("client:"+url[len(ReplaceStr01)+i:len(ReplaceStr01)+i+j1])
                    T1=url[len(ReplaceStr01)+i:len(ReplaceStr01)+i+j1]
        if y=="q=":#2
            #print("q=在第"+str(i)+"~"+str(len(ReplaceStr02)+i)+"位")
            urlBehind=url[len(ReplaceStr02): ]
            for j2 in range(0,len(urlBehind),1):
                z2=url[len(ReplaceStr02)+i+j2:len(ReplaceStr02)+i+j2+1]
                if z2=="":
                    print("q="+url[len(ReplaceStr02)+i:len(ReplaceStr02)+i+j2])
                    T2=url[len(ReplaceStr02)+i:len(ReplaceStr02)+i+j2]
                    break
    return T1,T2;

def replaceDict(url,dict):
    print(url.format(**dict))

