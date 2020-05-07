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


def print_tree(node, level, img, img2, todos, json_list):
    for title in node:
        spaces = ""
        i = 0
        while(i < level):
            spaces = "  " + spaces
            i = i + 1
        print(spaces + img +title)
        children = node[title]
        #
        kid = run_lenlist(todos, json_list, title)#改1
        if kid:
            kid.sort()
            for lenkid in kid:
                print(spaces + "  " + img2 + lenkid)
            else:
                pass
            
        #
        if len(children) > 0:
            for child in children:
                print_tree(child, level + 1, img, img2, todos, json_list)



def run_lenlist(json, jsonlist, parent):
    titlelist=[]
    a=0
    for tag in jsonlist:
        if tag == parent:
            jsondata=json[a]
            titlelist.append(jsondata["title"])
        a+=1
    return titlelist
        
     
