from src import Extractor, Cleaner, Analyzer




ex = Extractor()

page_names = ex.get_pages()

dataset = []
for page_name in page_names:
    data = {}

    page_html = ex.get_html(page_name)
    cleaner = Cleaner(page_html)


    data = {
        "keyword": cleaner.get_keyword(),
        "total_payment": cleaner.get_total_payment_stats(),
        "detailed_fixed_payment": cleaner.get_detailed_fixed_payment_stats(),
        "proposals": cleaner.get_number_of_proposals()
    }


    dataset.append(data)


analyzer = Analyzer(dataset)


analyzer.plot()