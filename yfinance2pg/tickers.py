import requests

<<<<<<< HEAD
#endpoint = 'https://www.sec.gov/include/ticker.txt'
#endpoint = 'http://www.e-swoosh.co.uk/apps/stocks/testticker.txt'

endpoint = 'http://www.e-swoosh.co.uk/apps/stocks/LSE.txt'


=======
>>>>>>> 9855a857ef376d69b02e6fa25a6cc558f6d630fb

def get_sec_list():
    endpoint = 'https://www.sec.gov/include/ticker.txt'
    tickers = []

    r = requests.get(endpoint)

    for line in r.text.split('\n'):
        tickers.append(line.split('\t')[0].upper())

    return tickers


def get_tickers_from_file(tickers_file):
    tickers = []

    with open(tickers_file) as f:
        for line in f:
            ticker = line.trim()
            if ticker != '':
                tickers.push(ticker)

    return tickers


def get_symbols(tickers_file):
    if tickers_file:
        get_tickers_from_file(tickers_file)

    return get_sec_list()
