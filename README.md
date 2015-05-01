# Nordpool

Data preprocessing / munging scripts for
[Nordpool](http://www.nordpoolspot.com/) power market data.

## Elspot

Download the Elspot hourly prices `.xls`-files that are really HTML-files.
Convert them to `.csv`-files using `elspot-prices-to-csv.py`
or convert to [SQLite](http://www.sqlite.org/)-format using `elspot-prices-to-sqlite.py`.
