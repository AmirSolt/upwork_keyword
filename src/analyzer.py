import matplotlib.pyplot as plt

class Analyzer:
    

    def __init__(self, dateset):
        self.dateset = dateset

        self.fig, self.axs = plt.subplots(2, 2)


    def plot_volumes(self):

        x = []
        y = []

        ax = self.axs[0,0]
        for data in self.dateset:
            volumes = data["total_payment"]["Hourly"] + data["total_payment"]["Fixed-Price"]
            x.append(data["keyword"])
            y.append(volumes)


        ax.set_title('Job Volume')
        ax.plot(x, y, "-o") 
        ax.set_xticklabels(labels=x, rotation=45, ha='right')


    def plot_fixed_prices(self):

        for data in self.dateset:

            x = []
            y = []

            ax = self.axs[0,1]
            for name, payemnt in data["detailed_fixed_payment"].items():
                x.append(name)
                y.append(payemnt)


            ax.set_title('Payment Distribution')
            ax.plot(x, y, "-o", label=data["keyword"])
            ax.legend(loc="upper right")
            ax.set_xticklabels(labels=x, rotation=45, ha='right')



    def plot_fixed_prices_by_total(self):

        for data in self.dateset:

            x = []
            y = []

            ax = self.axs[1,0]
            for name, payemnt in data["detailed_fixed_payment"].items():
                x.append(name)
                y.append(payemnt/data["total_payment"]["Fixed-Price"])


            ax.set_title('Payment Distribution / Fixed-Price')
            ax.plot(x, y, "-o", label=data["keyword"])
            ax.legend(loc="upper right")
            ax.set_xticklabels(labels=x, rotation=45, ha='right')



    def plot_proposals_by_total(self):

        for data in self.dateset:

            x = []
            y = []
            ax = self.axs[1,1]

            total = sum(data["proposals"].values())

            for name, proposal in data["proposals"].items():
                x.append(name)
                y.append(proposal/total)

            ax.set_title('Proposal Distribution by total')
            ax.plot(x, y, "-o", label=data["keyword"])
            ax.legend(loc="upper right")
            ax.set_xticklabels(labels=x, rotation=45, ha='right')





        


    def plot(self):
        self.plot_volumes()
        self.plot_fixed_prices()
        self.plot_fixed_prices_by_total()
        self.plot_proposals_by_total()

        plt.show()