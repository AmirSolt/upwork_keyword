import os




class Extractor:


    def __init__(self) -> None:
        pass


    def get_pages(self, folder="pages"):
        return [os.path.join(folder, f) for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


    def get_pages_html(self):
        for page in self.get_pages():
            yield self.open_html_file(page)


    def open_html_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    