import util2_05_09 as util
import json

if __name__ == '__main__':
    todo1 = util.read_json_file('D:/Spyder_import/data/todo-1.json')
    todo2 = util.read_json_file('D:/Spyder_import/data/todo-2.json')

    #print("todo 1:\n", todo1, sep='')
    #print("todo 2:\n", todo2, sep='')

    todos = todo1 + todo2
    #print("\ntodos:\n", json.dumps(todos, indent=4), sep='')
    #print("\ntodos:\n", todos)

    sorted_todos = util.sort(todos, "title")
    # print(sorted_todos)
    #print(json.loads(sorted_todos))
    
    #建立data目錄
    json_list = []
    for todo_data in todos:
        #print(todo_data["category"])
        json_list.append(todo_data["category"])
    #print(category_data)
    
    
    
    #print("\nsorted title:\n", json.dumps(sorted_todos, indent=4), sep='')

    #tag1 = 'Sports'
    #search_result = util.search_tag_basic(todos, 'tag', tag1)
    #print('\nsearch tag:' + tag1 + '\n', json.dumps(search_result, indent=4), sep='')

    #tag2 = 'Tennis'
    #search_result2 = util.search_tag(todos, 'tag', tag2)
    #print('\nsearch tag:' + tag2 + '\n', json.dumps(search_result2, indent=4), sep='')

    categories = util.read_json_file('D:/Spyder_import/data/category.json')
    categories = util.sort(categories, "title")
    #print("categories:", categories)
    relationDict = {}
    categoryDict = {}

    for category in categories:
        #print(category)
        if "parent" in category:
            relationDict[category["title"]] = category["parent"]
        category["children"] = []
        categoryDict[category["title"]] = category

    #print(categoryDict)
    #print(relationDict)

    tree = {}
    tree["root"] = []
    newDict = {}
    for title in categoryDict:
        #print(title)
        #print("category", category)
        #title = str(category.keys
        #print("title", title)
        if title in relationDict:
            #print(" title in relationDict")
            parentTitle = relationDict[title]
            #print(title, parentTitle)
            if title not in newDict:
                newDict[title] = {title:[]}
            #print(" parentTitle:" + parentTitle)
            if parentTitle in newDict:
                #print(" parentTitle in newDict")
                parentCat = newDict[parentTitle]
            else:
                #print(" parenttTitle not in newDict")
                parentCat = {parentTitle:[]}
                newDict[parentTitle] = parentCat
                #print(" new parentCat:", parentCat)
            parentCat[parentTitle].append(newDict[title])
            #print(" ", parentCat)
                #newDict[title] = parentCat
        
        else:
            #print(" title not in relationDict")
            #print(" ", newDict.get(title))
            if title not in newDict:
                newDict[title] = {title:[]}
            tree["root"].append(newDict[title])
    
    print("\n\n3:")
    print("\ntree:", tree)
    print_tree(tree, 0, "📁", "🗄", todos, json_list)

