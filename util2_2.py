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
