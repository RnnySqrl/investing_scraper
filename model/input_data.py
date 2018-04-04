import json
from json import JSONDecodeError

class Input_data(object):
    def __init__(self):
        pass

    def read_tickers(self):
        with open("model/files/tickers.txt", "r") as f:
            content = f.readlines()
            content = [x.strip() for x in content]
            if content:
                with open("model/files/tickers.json", "r") as json_data:
                    try:
                        data_tickers = json.load(json_data)
                    except JSONDecodeError as e:
                        print(e)
                    if data_tickers:
                        for ticker in content:
                            if ticker in data_tickers["tickers_info"].
                            # data_tickers["tickers_info"].append()
                    else:
                        data_tickers["tickers_info"] = list()

            return content
