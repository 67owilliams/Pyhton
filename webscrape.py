import bs4 as bs
import urllib.request
import lxml

url = urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_colors:_A%E2%80%93F").read()
soup = bs.BeautifulSoup(url, 'lxml')
table = soup.find_all('table')[0]
#print(table)
#for row in table.find_all('a'):
#    print(row.text)

table_rows = table.find_all('tr')
i = 0
name = []
for row in table_rows:
    a = row.find_all('a')
    data = [n.text for n in a]
    #print(name)
    td = row.find_all('td')
    data.extend([i.text for i in td])
    #print(row)
    name.insert(i, data)
    i+=1
for lists in name:
    print(lists)
