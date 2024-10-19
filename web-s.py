from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd


cService = Service("C:/Users/abasova/chromedriver/win64-129.0.6668.101/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service = cService)


products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the product
driver.get("https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq=")

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")
# for a in soup.findAll('a',href=True, attrs={'class':'_1YokD2 _3Mn1Gg'}):
for a in soup.findAll('div', attrs={'class':'_1YokD2 _3Mn1Gg'}):
    name = a.find('div', attrs={'class':'_4rR01T'})
    price = a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating = a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.text)
    ratings.append(rating.text)


df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
df.to_csv('products.csv', index=False, encoding='utf-8')

