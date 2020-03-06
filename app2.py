import util2


if __name__ == '__main__':
    file1 = 'todo-1.json'
    file2 = 'todo-2.json'
    json1 = loadJson(file1)
    json2 = loadJson(file2)
    newJson = mergeJson(json1, json2)
    #print(newJson)
    sortedList =sortTile(newJson)
    print(sortedList)
    DictSave(sortedList,'title')