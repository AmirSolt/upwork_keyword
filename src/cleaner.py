from bs4 import BeautifulSoup
import re





class Cleaner:


    def __init__(self, page_html) -> None:
        self.soup = BeautifulSoup(page_html, 'lxml')

    

    def get_keyword(self):
        path = ".flex-1>.up-input-group>div>div"
        keyword = self.soup.select_one(path).get("query")

        return keyword
    
    def get_job_payment_stats(self):
        path_name = 'div[data-test="filter-sidebar-component_jobType"] > div:first-child label span:not([class])'
        path_number = 'div[data-test="filter-sidebar-component_jobType"] > div:first-child label span:not([class]) small'


        payment_names = self.soup.select(path_name).getText()
        payment_amounts = self.soup.select(path_number).getText()
        payment_amounts = [self.__extract_number_from_text(payment) for payment in payment_amounts]

        return dict(zip(payment_names, payment_amounts))
        


    def get_number_of_proposals(self):
        path_name = 'div[data-test="filter-sidebar-component_proposals"] > div:first-child label span:not([class])'
        path_number = 'div[data-test="filter-sidebar-component_proposals"] > div:first-child label span:not([class]) small'


        proposal_names = self.soup.select(path_name).getText()
        proposal_amounts = self.soup.select(path_number).getText()
        proposal_amounts = [self.__extract_number_from_text(proposal) for proposal in proposal_amounts]

        return dict(zip(proposal_names, proposal_amounts))
        






    def __extract_number_from_text(self, text):
        return int(re.sub(r'\D', '', text))