import json
def loadJson( fileName):
	with open("C:\\Users\\user\\Desktop\\"+fileName, 'r') as f2:
		ret = json.load(f2)
	return ret


def mergeJson( json1,  json2):
	json = json1 + json2
	return json


def sortTile( newJson):
    return sorted(newJson, key=lambda k: k.get('title'))


def DictSave( sortedList, label):
    print( label )
    for i in range( 0, len( sortedList )):
        print( sortedList[ i ][ label ] )
        

def query_parameter( url):
    idx = url.find("{")
    query_str = url[ idx + 1 :]
    split_str = query_str.split(",")
    ret = {}#對應次要目錄用途
    list_1 = ""
    label = ""
    Test=0 #確認無parent
    for str in split_str:
        split_again = str.split(":")
        key = split_again[0]
        value = split_again[1]
        value = value.rstrip("}").strip().rstrip("'").lstrip("'")
        key = key.strip().rstrip("'").lstrip("'")#過濾多餘
        if key == "title" and label != "":
            ret[value] = label
        if key == "parent":
            Test=Test+1
            label = value     
    if key == "title" and Test==0:
        list_1 = value
    
    return list_1, ret

        
        
        


def RunLen( sortedList_2):
    list_1 = [] #主目錄
    list_2 = {} #次要目錄位置對應
    for sortedListLen_2 in sortedList_2:
        list,ret = query_parameter( str( sortedListLen_2))
        if list != "":
            list_1.append( list)
        else:
            list_2 = {**list_2, **ret}
    print("次目錄對應辭典:", list_2)
    print("主目錄:", list_1)
    print("目錄:")
    for i in list_1:
        print( i )
        for j in list_2.keys():
            if i == list_2[j]:
                print("-",j)
                

        
        
        



    

    
    
