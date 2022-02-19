class Global:
    def __init__(self, response):
        self.NewConfirmed = response["NewConfirmed"]
        self.TotalConfirmed = response["TotalConfirmed"]
        self.NewDeaths = response["NewDeaths"]
        self.TotalDeaths = response["TotalDeaths"]
        self.NewRecovered = response["NewRecovered"]
        self.TotalRecovered = response["TotalRecovered"]
