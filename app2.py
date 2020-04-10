#import util2


if __name__ == '__main__':
    file1 = 'todo-1.json'
    file2 = 'todo-2.json'
    file3 = 'todo-3.json'
    json1 = loadJson(file1)
    json2 = loadJson(file2)
    json3 = loadJson(file3)
    newJson = mergeJson(json1, json2)
    #print(newJson)
    sortedList =sortTile(newJson)
    sortedList_2 =sortTile(json3)
    print("\n#1")
    print(sortedList)
    print("\n#2")
    print("jason:\n",sortedList_2)
    RunLen(sortedList_2)
    print("\n#3")
    DictSave(sortedList,'title')
    