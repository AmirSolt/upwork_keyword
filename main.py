from src import Extractor, Cleaner, Grapher, Analyzer, Storage



ex = Extractor()
st = Storage()

page_names = ex.get_pages()

dataset = []
for page_name in page_names:
    data = {}

    if st.check_if_file_exists(page_name):
        data = st.load_from_json(page_name)

    else:

        page_html = ex.get_html(page_name)
        cleaner = Cleaner(page_html)


        data = {
            "keyword": cleaner.get_keyword(),
            "total_payment": cleaner.get_total_payment_stats(),
            "detailed_fixed_payment": cleaner.get_detailed_fixed_payment_stats(),
            "proposals": cleaner.get_number_of_proposals()
        }

        st.save_as_json(data, page_name)

 


    dataset.append(data)





analyzer = Analyzer(dataset)
# analyzer.get_filter_bad_proposals()
print("===================PROPOSALS=================")
analyzer.order_by_proposal()
analyzer.print_dataset(keyword="proposal_score")
print("===================PAYEMNT=================")
analyzer.order_by_payment()
analyzer.print_dataset(keyword="payment_score")
print("===================TOTAL SCORE=================")
analyzer.order_by_total_score()
analyzer.print_dataset(keyword="total_score")





grapher = Grapher(dataset)
grapher.plot()
