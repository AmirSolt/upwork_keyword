from src import Extractor, Cleaner, Analyzer, Storage




ex = Extractor()
st = Storage()

page_names = ex.get_pages()


for page_name in page_names:
    data = {}
    if st.check_if_file_exists(page_name):
        data = st.load_from_json(page_name)

    else:
        page_html = ex.get_html(page_name)
        cleaner = Cleaner(page_html)


        data = {
            "keyword": cleaner.get_keyword(),
            "total_payment_stats": cleaner.get_total_payment_stats(),
            "detailed_fixed_payment_stats": cleaner.get_detailed_fixed_payment_stats(),
            "number_of_proposals": cleaner.get_number_of_proposals()
        }

        st.save_as_json(data, page_name)