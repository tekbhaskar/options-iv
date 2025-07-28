import pandas as pd

def load_sp500_tickers():
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    tables = pd.read_html(url)
    return tables[0]['Symbol'].tolist()

def load_nyse_tickers():
    url = 'https://old.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download'
    df = pd.read_csv(url)
    return df['Symbol'].dropna().unique().tolist()