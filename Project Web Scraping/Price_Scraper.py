import requests
from bs4 import BeautifulSoup as bs

url = 'https://www.amazon.in/Auroral-Storage-Additional-Exchange-Offers/dp/B07X9YNV5Y/ref=sr_1_2?dchild=1&keywords=oppo+reno+3&qid=1608092672&sr=8-2'



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
page = requests.get(url,headers=headers)
soup = bs(page.content,'html.parser')
a = soup.find(id="productTitle")
b = a.get_text()
print("AMAZON")
price = soup.find('span',id="priceblock_dealprice")
if price is None:
    price = soup.find(id="priceblock_ourprice")
price = price.get_text()
print(b.strip(),price)


res = requests.get('https://www.flipkart.com/oppo-reno3-pro-auroral-blue-128-gb/p/itm05804cb14fc19?pid=MOBFPYA4RSKUJZPH&lid=LSTMOBFPYA4RSKUJZPHZAKDFH&marketplace=FLIPKART&srno=s_1_1&otracker=search&otracker1=search&fm=SEARCH&iid=eb83cd1c-9840-45e6-96d5-723a8c8a1ed5.MOBFPYA4RSKUJZPH.SEARCH&ppt=sp&ppn=sp&ssid=g77pcixho00000001608092679595&qH=2ac5a97bf2a7ed35')
soup = bs(res.text,'lxml')
print("FLIPKART")
name = soup.find('span', class_ = 'B_NuCI').get_text()
cost = soup.find('div', class_ = '_30jeq3 _16Jk6d').get_text()
print(name,cost)