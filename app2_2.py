import json

if __name__ == '__main__':
	categories = read_json_file('C:\\Users\\user\\Desktop\\todo-3.json')
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
	tree["root"] = [];
	newDict = {}
	for title in categoryDict:
		#print("category", category)
		#title = str(category.keys
		#print("title", title)
		if title in relationDict:
			parentTitle = relationDict[title]
			#print(title, parentTitle)

			newDict[title] = {"title": title}
			if parentTitle in newDict:
				parentCat = newDict[parentTitle]
				parentCat["children"].append(newDict[title])
			else:
				parentCat = {}
				parentCat["title"] = parentTitle
				parentCat["children"] = []
				newDict[parentTitle] = parentCat
		else:
			newDict[title] = {"title": title, "children":[]}
			tree["root"].append(newDict[title])

	#print("tree:", tree)
print("目錄:")
for i in range(len(tree['root'])):
    print(tree['root'][i]['title'])
    for j in range(len(tree['root'][i])):
        print("-"+tree['root'][i]['children'][j]['title'])
