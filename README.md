# What is this monster?

docker-compose up

1. database will be created

2. Get some data from yahoo finance on this box:

- `cd .\yfinance2pg\`
- `C:\users\paul\AppData\Local\Programs\Python\Python38\python.exe save_data_to_csv.py -symbol X7PS -time_window daily`








# yfinance2pg

Download financial data to postgres database from yahoo finance.

```txt
yfinance2pg
    Download financial data to postgres database from yahoo finance.

usage:
    yfinance2pg <options>

options:
    --help
        help menu
    --exclude [value ...]
        skip download phase, possible list
        values are `companies` or `priceVolume`
    --start-date [YYYY-MM-DD]
        start date for price volume data download
        defaults to last downloaded day, or Jan 1, 1970
        if no previous data exists
    --host [string]
    --user [string]
    --dbname [string]
    --port [string]
    --password [string]
        postgres connection options
```

## Want to contribute?

Open a PR!
