import json



def load_json_file(path):
    with open(path) as fh:
        j_obj = json.load(fh)
    return j_obj


def add_content(obj):
    print("fuck")
    j_obj = load_json_file('test.json')
    print(j_obj)
    list_menuitem = j_obj['menu']['popup']['menuitem']
    j_obj['menu']['popup']['menuitem'].append(obj)
    # list_menuitem.append(obj)
    # j_obj.pop(list_menuitem)
    # print(list_menuitem)
    with open('test.json', 'w') as fh:
        json.dump(j_obj, fh)


if __name__ == '__main__':
    obj = {
        "value": "Old",
        "onclick": "RemoveOldDoc()"
    }
    # load_json_file('test.json')
    add_content(obj)

