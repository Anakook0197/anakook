from bs4 import BeautifulSoup
import requests
import mysql.connector

con = mysql.connector.connect(user='root',host='localhost',password='4170',database= 'Amazon',auth_plugin='mysql_native_password')
cur = con.cursor()

url = "https://www.amazon.in/SanDisk-Ultra-Dual-64GB- Drive/dp/B01N6LU1VF?ref_=Oct_d_omwf_d_1375411031_1&pd_rd_w=Sznli &content-id=amzn1.sym.6d876bf1-3cdb-4dbe-a7f1- 92ba8ba5547b&pf_rd_p=6d876bf1-3cdb-4dbe-a7f1- 92ba8ba5547b&pf_rd_r=PT6JYTTZ1N339K3CJRJ7&pd_rd_wg=5mQwL&pd_rd_r=2d9f8d76-9846-44a1-8647-bf588466d1c0&pd_rd_i=B01N6LU1VF"

header = {"Connection":"close","Upgrade-Insecure-Requestes":"1","User- Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"}
page = requests.get(url,headers=header)

soup1 = BeautifulSoup(page.content,"html.parser")
soup2 = BeautifulSoup(soup1.prettify(),"html.parser")
title = soup2.find(id="productTitle").get_text().strip().replace(" ","")
price = soup2.find('span',attrs={'class':"a- offscreen"}).get_text().strip().replace(" ","").replace("?","")
ratting = soup2.find(id="acrCustomerReviewText").get_text().strip().replace(" ","")

"""
print(title)
print(price)
print(ratting)

"""
product_info="insert into products (name,price,ratting) values"
val = (title,price,ratting)
cur.execute(product_info,val)
con.commit()
con.close()
print('success')




