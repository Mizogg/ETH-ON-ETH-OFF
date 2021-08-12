#ethtxchecker.py Mizogg 07/08/2021 mizogg.co.ukCheck ETH Address list for Transactions Made by mizogg.co.uk
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import itertools
import random
import requests

print('ETH address list loading please wait..................................:')

with open("eth.txt", "r") as file:
    line_count = 0
    for line in file:
        line != "\n"
        line_count += 1
print('Total Addresses Loaded:', line_count)       
mylist = []

with open('ethlist.txt', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

count=0
remaining=line_count
for i in range(0,len(mylist)):
    api1="?apiKey=freekey"
    api2="?apiKey=freekey"
    #api3="?apiKey=freekey"
    #api4="?apiKey=freekey"
    #api5="?apiKey=freekey"
    #api6="?apiKey=freekey"
    mylistapi = [str(api1), str(api2)]
    #mylistapi = [str(api1), str(api2), str(api3), str(api4), str(api5), str(api6)]
    apikeys=random.choice(mylistapi)
    ethadd = mylist[i]
    blocs=requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd +apikeys)
    ress = blocs.json()
    TXS = dict(ress)["countTxs"]
    count+=1
    remaining-=1
    print ( 'Ethereum Address:  ', ethadd,  '  : TX = ',  str(TXS), '  = Scan Number: ', str(count), '  = Remaining:  ', str(remaining),  end='\r')
    if int(TXS) > 0:
        print ('Ethereum Address    :  '  + ethadd +  '  : TX = '  +  str(TXS))
        f=open("winner.txt","a")
        f.write('\n Eth Address: ' + ethadd +  '  : TX = '  +  str(TXS))
        f.close()
