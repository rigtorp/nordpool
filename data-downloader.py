import os.path
import requests

urls = [
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/elspot-prices_2013_hourly_eur.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/elspot-prices_2014_hourly_eur.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/elspot-prices_2015_hourly_eur.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/elspot-volumes_2013_hourly.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/elspot-volumes_2014_hourly.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/elspot-volumes_2015_hourly.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/regulating-prices_2013_hourly_eur.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/regulating-prices_2014_hourly_eur.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/regulating-prices_2015_hourly_eur.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/regulating-volumes_2013_hourly.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/regulating-volumes_2014_hourly.xls',
    'http://www.nordpoolspot.com/globalassets/marketdata-excel-files/regulating-volumes_2015_hourly.xls']

for url in urls:
    fname = os.path.basename(url)
    if not os.path.isfile(fname):
        print url
        r = requests.get(url)
        open(fname, 'w').write(r.content)
