import json


def read_json_file(file_name):
	with open(file_name) as json_file:
		data = json.load(json_file)
		return data


def sort(json_data, sort_by):
	json_data = sorted(json_data, key=lambda k: k.get(sort_by, 0))
	return json_data


def search_tag_basic(todos, search_attribute, search_value):
	ret = []
	for todo in todos:
		if todo[search_attribute].find(search_value) != -1:
			ret.append(todo)
	return ret


def search_tag(todos, search_attribute, search_value):
	ret = list(filter(lambda todo: todo[search_attribute].find(search_value) != -1, todos))
	return ret


def print_tree(node, level, img, img2, todos,imgmath):#imgmath:1,是檔案 0,不是檔案
    children=[]
    for title in node:
        spaces = ""
        i = 0
        while(i < level):
                spaces = "  " + spaces
                i+=1
        #print(spaces + img +title)
        if title=="1":
            imgmath=1
            children = node[title]
            if len(children) > 0:
                for child in children:
                    print_tree(child, level+1, img, img2, todos,imgmath)
        elif imgmath==0:
            print(spaces + img +title)
        elif imgmath==1:
            print(spaces + img2 +title)
        children = node[title]
        if len(children) > 0 and imgmath==0: #判斷不是檔案
            for child in children:
                print_tree(child, level + 1, img, img2, todos,0)

        
     
