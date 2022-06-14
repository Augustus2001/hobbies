#BasicWebScraping.py
#<div class="col-xs-6 col-xs-offset-6 colorRed"><h1>38.00</h1></div>
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
def StockPrice(code):
    url=f"https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={code}&ssoPageId=9&selectPage=1"
    webopen=req(url)
    page_html=webopen.read()
    webopen.close()
    #print(page_html)
    data=soup(page_html,'html.parser')
    result=data.findAll("div",{"class","col-xs-6"})
    print(result[1].text.replace("\n","").replace("\r","")) #ราคาล่าสุด
    text1=result[1].text.replace("\n","").replace("\r","")
    text1=text1[0:10]
    print(result[2].text.replace("\n","").replace("\r","")) #38.00
    price=result[2].text.replace("\n","").replace("\r","")
    print(result[3].text.replace("\n","").replace(" ","").replace("\r",'')) #เปลี่ยนเเปลง-0.25
    change=result[3].text.replace("\n","").replace(" ","").replace("\r",'')
    print(result[4].text.replace("\n","").replace(" ","").replace("\r",'')) #เปลี่ยนเเปลง -0.65%
    percen_change=(result[4].text.replace("\n","").replace(" ","").replace("\r",""))
    percen_change=float(percen_change[12:len(percen_change)-1])
    print(percen_change)
    price=(float(price))
    change=(float(change[11:]))
    print(f"Stock :{text1}  price:{price} change:{change} percen:{percen_change}%")
    return
StockPrice("aot")