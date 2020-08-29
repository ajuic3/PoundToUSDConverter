import requests
from bs4 import BeautifulSoup
import os

URL = 'https://www.foreignexchange.org.uk/fx-rates/conversion/1/GBP/USD'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='dataDisplay')
#print(soup)
#print(results.prettify())
conversion = results.find_all('td', attrs={"style": "font-size:17px;color:#000;"})
print("\n" + str(conversion[0]))
print("\nData sourced from: https://www.foreignexchange.org.uk/.")

try:
    x = int(input("\nHow many pounds do you need?: "))
    y = float(input("Enter the conversion rate: "))
    product = x * y
    print("\nIt will cost: $"+ str(product)+ " to transfer "+ str(x) + " pounds.")
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)

moneyRate = open("conversion.txt" , "w")
moneyRate.write("\n" + str(conversion[0]))
moneyRate.write("\n")
moneyRate.write("\nIt will cost: $"+ str(product)+ " to transfer "+ str(x) + " pounds.")
moneyRate.close()
os.system("pause")
