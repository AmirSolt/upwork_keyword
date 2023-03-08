from bs4 import BeautifulSoup
import re




class Cleaner:


    job_type_group = 'div[data-test="filter-sidebar-component_jobType"]'


    def __init__(self, page_html) -> None:
        self.soup = BeautifulSoup(page_html, 'html.parser')


    def get_keyword(self):
        path = 'div[data-test="UpCTypeahead"] > div'
        element = self.soup.select_one(path)
        keyword = element.get("query")
        
        return keyword
    

    def get_job_payment_stats(self):
        path_name = f'{self.job_type_group} label span:not([class])'
        path_number = f'{self.job_type_group} label span:not([class]) small'


        payment_names = self.__textify_list_of_elements(self.soup.select(path_name))
        payment_amounts =  self.__textify_list_of_elements(self.soup.select(path_number))
        payment_amounts = [self.__extract_number_from_text(payment) for payment in payment_amounts]

        return dict(zip(payment_names, payment_amounts))
    

    def get_total_payment_stats(self):
        return {k:v for k, v in self.get_job_payment_stats().items() if k == "Fixed-Price" or k == "Hourly"}
        
    def get_detailed_fixed_payment_stats(self):
        return {k:v for k, v in self.get_job_payment_stats().items() if k != "Fixed-Price" and k != "Hourly"}


    def get_number_of_proposals(self):
        path_name = 'div[data-test="filter-sidebar-component_proposals"] label span:not([class])'
        path_number = 'div[data-test="filter-sidebar-component_proposals"] label span:not([class]) small'


        proposal_names = self.__textify_list_of_elements(self.soup.select(path_name))
        proposal_amounts = self.__textify_list_of_elements(self.soup.select(path_number))
        proposal_amounts = [self.__extract_number_from_text(proposal) for proposal in proposal_amounts]

        return dict(zip(proposal_names, proposal_amounts))
        




    def __textify_list_of_elements(self, elements):
        return [self.__clean_text(element.find(text=True, recursive=False)) for element in elements]
    
    def __clean_text(self, text):
        return re.sub(r'\s+', ' ', text).strip()

    def __extract_number_from_text(self, text):
        return int(re.sub(r'\D', '', text))