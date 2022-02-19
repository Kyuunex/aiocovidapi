import dateutil.parser

from aiocovidapi.SummaryCountry import SummaryCountry
from aiocovidapi.Global import Global


class Summary:
    def __init__(self, response):
        self.Date = dateutil.parser.parse(response["Date"])
        self.Global = Global(response["Global"])
        self.Countries = []
        for country in response["Countries"]:
            self.Countries.append(SummaryCountry(country))
