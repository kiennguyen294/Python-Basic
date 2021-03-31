import json


class Updatejson:
    print('test')
    obj_file = None

    def __init__(self, obj_update, path):
        self.obj_update = obj_update
        self.path = path

    def _load_json_file(self):
        with open(self.path) as fh:
            obj_file = json.load(fh)
        return obj_file
        # print('load json file')

    def modify_json_file(self):
        new_obj_file = None
        obj_file = self._load_json_file()
        print(obj_file)
        print('modify json file')

    def update_json_file(self):
        print('update json file')


def main():
    path = 'example.json'
    obj_update = {
        "value": "Old",
        "onclick": "RemoveOldDoc()"
    }
    a = Updatejson(obj_update, path)
    #a.load_json_file()
    a.modify_json_file()
    a.update_json_file()


if __name__ == '__main__':
    main()
