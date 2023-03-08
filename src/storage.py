
import json
import os


class Storage:


    def if_folder_doesnt_exist_create(self, folder_name):
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

    def check_if_file_exists(self, page_name):
        self.if_folder_doesnt_exist_create("data")
        return os.path.isfile(self.__get_file_path(page_name))


    def load_from_json(self, page_name):

        with open(self.__get_file_path(page_name), 'r') as f:
            return json.load(f)

    def save_as_json(self, data, page_name):

        with open(self.__get_file_path(page_name), 'w') as f:
            json.dump(data, f, indent=4)


    def __get_file_path(self, page_name):
        return "data/"+page_name.replace(".html", ".json")