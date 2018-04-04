from model.input_data import Input_data
from controller.investing import Investing

#obtain the tickers that we want to scrape
tickers = Input_data().read_tickers()
invest = Investing(tickers)
invest.start()
