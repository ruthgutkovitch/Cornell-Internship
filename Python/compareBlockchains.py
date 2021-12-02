import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
from datetime import datetime
import numpy as np
import pandas as pd
import csv

cardano = "/home/ruth/NFT-study/Ruth/Cardano/Data/ADA-USD.csv"
ethereum = "/home/ruth/NFT-study/Ruth/Ethereum/Data/Ethereum Historical Data.csv"
solana = "/home/ruth/NFT-study/Ruth/Solana/Data/Solana Historical Data.csv"
polygon = "/home/ruth/NFT-study/Ruth/Polygon/Matic Historical Data.csv"

#Explanation:
#Date,Price,Open,High,Low,Volume,Change %
#2016-03-10,11.75,11.2,11.85,11.07,0.00K,4.91%
#Price, Open, High, and Low - We need to remove the commas(,) from the values inorder to let python process the whole value
#Volume - M denotes Million, we need to convert 1.70M to 1700000, and Thousands(K)
#Change % - Need to remove the percentage symbol (-2.06% to -2.06)

def processData():
    files = [#ethereum, solana, polygon,
    polygon]
    for file in files:
        data = pd.read_csv(file)
        data['Volume'] = data['Volume'].astype(str).replace("-",np.nan)
        data["Volume"] = (data["Volume"].astype(str).replace(r'[KM]+', '', regex=True).astype(float) * \
            data["Volume"].str.extract(r'[\d\.]+([KM]+)', expand=False)
                .fillna(1)
             .replace(['K','M'], [10**3, 10**6]).astype(int))     

        data["Price"]=data["Price"].astype(str).str.extract("([0-9,]+\.?[0-9]+)").replace(',','', regex=True).astype("float")
        data["Open"]=data["Open"].astype(str).str.extract("([0-9,]+\.?[0-9]+)").replace(',','', regex=True).astype("float")
        data["High"]=data["High"].astype(str).str.extract("([0-9,]+\.?[0-9]+)").replace(',','', regex=True).astype("float")
        data["Low"]=data["Low"].astype(str).str.extract("([0-9,]+\.?[0-9]+)").replace(',','', regex=True).astype("float")
        data["Change %"] = data["Change %"].astype(str).str.extract("([-]?[0-9]+\.?[0-9]+)").astype("float")
        data.to_csv(file, index=False)

        data=data.dropna()
            

def drawPlots():

    df3 = pd.read_csv(cardano)
    r3 = plt.plot(df3['Date'],df3['Volume'],color='blue',label='Cardano')
    df1 = pd.read_csv(ethereum)
    r1 = plt.plot(df1['Date'],df1['Volume'],color='orange',label='Ethereum')

    df2 = pd.read_csv(solana)
    r2 = plt.plot(df2['Date'],df2['Volume'], color='red',label='Solana')

   
    plt.xlabel('Date', fontsize='11')
    plt.xticks(df1['Date'])
    plt.ylabel('Volumes', fontsize='11')
    plt.title('Volume Trends', fontsize='28')
    #plt.grid()
    plt.legend(loc='upper right')
    plt.savefig("/home/ruth/NFT-study/Ruth/Plots/blockchains")




    

    


if __name__ == "__main__":
    #processData() - convert polygon
    drawPlots()