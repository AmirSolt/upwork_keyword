import os




class Extractor:


    def __init__(self) -> None:
        pass


    def get_pages(self, folder="pages"):
        return [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


   


    def get_html(self, page_name, folder="pages"):
        with open(folder+"/"+page_name, 'r', encoding='utf-8') as f:
            return f.read()
    