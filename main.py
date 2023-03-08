from src import Extractor, Cleaner, Analyzer




ex = Extractor()

pages_html = ex.get_pages_html()


for page_html in pages_html:
    cleaner = Cleaner(page_html)
    print(cleaner.get_keyword())
    print(cleaner.get_total_payment_stats())
    print(cleaner.get_detailed_fixed_payment_stats())
    print(cleaner.get_number_of_proposals())
    print(">>>>>>")

