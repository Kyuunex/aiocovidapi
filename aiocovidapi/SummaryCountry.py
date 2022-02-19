import dateutil.parser


class SummaryCountry:
    def __init__(self, response):
        self.Country = response["Country"]
        self.CountryCode = response["CountryCode"]
        self.Slug = response["Slug"]
        self.NewConfirmed = response["NewConfirmed"]
        self.TotalConfirmed = response["TotalConfirmed"]
        self.NewDeaths = response["NewDeaths"]
        self.TotalDeaths = response["TotalDeaths"]
        self.NewRecovered = response["NewRecovered"]
        self.TotalRecovered = response["TotalRecovered"]
        self.Date = dateutil.parser.parse(response["Date"])

    def __str__(self):
        return self.Country
