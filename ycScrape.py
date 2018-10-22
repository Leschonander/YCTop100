import csv
import requests
from bs4 import BeautifulSoup

url = 'https://www.ycombinator.com/topcompanies/'
csvFile = 'yc100.csv'


req = requests.get(url)
soup = BeautifulSoup(req.text, 'html.parser')

name = [item['data-name'] for item in soup.find_all('div', attrs={'data-name' : True})]
rank = [item['data-rank'] for item in soup.find_all('div', attrs={'data-rank' : True})]
sectors = [item['data-sectors'] for item in soup.find_all('div', attrs={'data-sectors' : True})]
jobs = [item['data-jobs-created'] for item in soup.find_all('div', attrs={'data-jobs-created' : True})]
batch = [item['data-batch-season'] for item in soup.find_all('div', attrs={'data-batch-season' : True})]
year = [item['data-batch-year'] for item in soup.find_all('div', attrs={'data-batch-year' : True})]


jobs = list(map(int, jobs))
batch = list(map(int, batch))
year = list(map(int, year))
rows = zip(name, rank, sectors, jobs, batch, year)

with open('yc100.csv', 'w') as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)
