import sys
from bs4 import BeautifulSoup

def main(fname):
    soup = BeautifulSoup(open(fname))
    out = open(fname[:-4] + '.csv', 'w')
    header1 = [cell.get_text().strip().encode('ascii', 'ignore') for cell in
        soup.find('thead').find_all('tr')[-2].find_all('td')]
    header1 = [x for y in zip(header1, header1) for x in y]
    header2 = [cell.get_text().strip().encode('ascii', 'ignore') for cell in
        soup.find('thead').find_all('tr')[-1].find_all('td')]
    header = [x+y for x,y in zip(header1, header2)]
    header = ['Date'] + header[1:]
    out.write(','.join(header) + '\n')
    data = [[cell.get_text().strip().replace(',', '.') for cell in row.find_all('td')]
           for row in soup.find('tbody').find_all('tr')]
    for row in data:
        date = row[0][-4:] + '-' + row[0][:5]
        hour = row[1][:2]
        out.write(','.join([date, hour] + row[2:]) + '\n')
    

if __name__ == "__main__":
    main(sys.argv[1])
