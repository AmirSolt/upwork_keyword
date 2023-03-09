
from pprint import pprint


class Analyzer:


    MIN_PROPOSALS = 50


    def __init__(self, dataset) -> None:
        self.dataset = dataset




    def get_filter_low_proposals(self):
        n_dataset = []
        for data in self.dataset:
            if list(data["proposals"].values())[0] > self.MIN_PROPOSALS:
                n_dataset.append(data)

        self.dataset = n_dataset
    





    def order_by_proposal(self):

        proposal_len = len(self.dataset[0]["proposals"].values())

        for i, data in enumerate(self.dataset):
            score = 0


            total = sum(data["proposals"].values())

            for j, proposal in enumerate(data["proposals"].values()):
                score += (proposal/total)*(proposal_len-(j+1))


            self.dataset[i]["proposal_score"] = score 


        self.dataset = sorted(self.dataset, key=lambda x: x["proposal_score"], reverse=True)


    def order_by_payment(self):
        for i, data in enumerate(self.dataset):
            score = 0
            total = data["total_payment"]["Fixed-Price"]
            for j, payment in enumerate(data["detailed_fixed_payment"].values()):
                score += (payment/total)*(j+1)


            self.dataset[i]["payment_score"] = score 


        self.dataset = sorted(self.dataset, key=lambda x: x["payment_score"], reverse=True)



    def order_by_total_score(self):

        sum_payment_score = sum([data["payment_score"] for data in self.dataset])
        sum_proposal_score = sum([data["proposal_score"] for data in self.dataset])

        for i, data in enumerate(self.dataset):
            score = 0
            score = self.dataset[i]["payment_score"]/sum_payment_score + self.dataset[i]["proposal_score"]/sum_proposal_score
            self.dataset[i]["total_score"] = score


        self.dataset = sorted(self.dataset, key=lambda x: x["total_score"], reverse=True)



    def print_dataset(self, keyword=None):

        if keyword:
            kws = [(data["keyword"],data[keyword]) for data in self.dataset]
        else:
            kws = [data["keyword"] for data in self.dataset]
        pprint(kws)
