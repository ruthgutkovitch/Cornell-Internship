import matplotlib.pyplot as plt
import matplotlib.dates as mpl_dates
import pandas as pd

cardano = "/home/ruth/NFT-study/Ruth/Cardano/Data/ADA-USD.csv"
ethereum = "/home/ruth/NFT-study/Ruth/Ethereum/Data/Ethereum Historical Data.csv"
solana = "/home/ruth/NFT-study/Ruth/Solana/Data/Solana Historical Data.csv"
polygon = "/home/ruth/NFT-study/Ruth/Polygon/Matic Historical Data.csv"

df = pd.read_csv(ethereum)
fig, ax = plt.subplots(figsize=(20,8))
ax.bar(df['Date'], df['Volume'])
ax.xaxis.set_major_locator(plt.MaxNLocator(15))
ax.set_xlabel('Date', fontsize='11')
ax.set_ylabel('Volumes', fontsize='11')
plt.title('Volume Trends', fontsize='28')
plt.grid()
plt.savefig("/home/ruth/NFT-study/Ruth/Plots/ethereum")
