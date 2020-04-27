# process.py>


def processfunction(checkedlist):
    print("\nfromt inside process\n")
    print(checkedlist)
    print("-----------------------------------------------------")
    import requests
    from bs4 import BeautifulSoup
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import json
    dic = {}
    URL = []
    if 'stock1' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/auto-2-3-wheelers/heromotocorp/HHM"
        URL.append(tag)
    if 'stock2' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI"
        URL.append(tag)
    if 'stock3' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/banks-public-sector/statebankindia/SBI"
        URL.append(tag)
    if 'stock4' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/hdfcbank/HDF01"
        URL.append(tag)
    if 'stock5' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/computers-software/tataconsultancyservices/TCS"
        URL.append(tag)
    if 'stock6' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/icicibank/ICI02"
        URL.append(tag)
    if 'stock7' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/finance-leasinghire-purchase/bajajfinance/BAF"
        URL.append(tag)
    if 'stock8' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/banks-private-sector/axisbank/AB16"
        URL.append(tag)
    if 'stock9' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/food-processing/britanniaindustries/BI"
        URL.append(tag)
    if 'stock10' in checkedlist:
        tag = "https://www.moneycontrol.com//india/stockpricequote/paintsvarnishes/asianpaints/AP31"
        URL.append(tag)
    if 'stock11' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/computers-software/infosys/IT"
        URL.append(tag)
    if 'stock12' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/telecommunications-service/bhartiairtel/BA08"
        URL.append(tag)
    if 'stock13' in checkedlist:
        tag = "https://www.moneycontrol.com/india/stockpricequote/personal-care/hindustanunilever/HU"
        URL.append(tag)
    i = 0
    for tag in URL:
        response = requests.get(tag, timeout=240)
        soup = BeautifulSoup(response.content, "html.parser")
        elem = soup.find('div', attrs={'class': 'pcnsb div_live_price_wrap'})
        s = elem.find_next()
        print(float(s.get_text()))
        print(soup.find("h1").text)
        dic[i] = {'CompanyName': soup.find(
            "h1").text, 'StockValue': float(s.text)}
        i = i+1
    print('number of companies', len(URL))
    for j in dic.values():
        print(j)

    df = pd.DataFrame.from_dict(dic, orient='index', columns=[
                                'CompanyName', 'StockValue'])

    df.plot(x='CompanyName', y='StockValue', kind='line')
    df.plot(x='CompanyName', y='StockValue', kind='bar')
    plt.show()
    return dic
