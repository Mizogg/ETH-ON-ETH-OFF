# ethprivatekey.py Check Private Keys from File convert to Address and check Transactions. Online API Get FREE API KEY from https://ethplorer.io/
# Good Luck and Happy Hunting. Made by mizogg.co.uk 12/08/2021
# Donations 3M6L77jC3jNejsd5ZU1CVpUVngrhanb6cD
import sys
from ecdsa import SigningKey, SECP256k1
import sha3
import random
import requests

with open("ethprivatekey.txt", "r") as file:
    line_count = 0
    for line in file:
        line != "\n"
        line_count += 1
print('Total Addresses Loaded:', line_count)       
mylist = []

with open('ethprivatekey.txt', newline='', encoding='utf-8') as f:
    for line in f:
        mylist.append(line.strip())

count=0
remaining=line_count
for i in range(0,len(mylist)):
    count+=1
    remaining-=1
    api1="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
    api2="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
    #api3="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
    #api4="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
    #api5="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
    #api6="?apiKey=freekey" # Get FREE API KEY from https://ethplorer.io/
    mylist1 = [str(api1), str(api2)] # 2 API KEYS
    #mylist = [str(api1), str(api2), str(api3), str(api4)] # 4 API KEYS
    #mylist = [str(api1), str(api2), str(api3), str(api4), str(api5), str(api6)] # 6 API KEYS
    apikeys=random.choice(mylist1)
    hex_priv_key = mylist[i]
    keccak = sha3.keccak_256()
    priv = SigningKey.from_string(string=bytes.fromhex(hex_priv_key), 
                              curve=SECP256k1)
    pub = priv.get_verifying_key().to_string()
    keccak.update(pub)
    kec = keccak.hexdigest()[24:]
    ethadd = '0x' + kec
    privatekey = priv.to_string().hex()
    blocs=requests.get("https://api.ethplorer.io/getAddressInfo/" + ethadd +apikeys)
    ress = blocs.json()
    TXS = dict(ress)["countTxs"]
    #print ( 'Ethereum Address    :  ', ethadd,  '  : TX = ',  str(TXS), end='\r')
    #print('\nPrivate key: ', priv.to_string().hex(), '\nAddress: ', ethadd, '  : TX = '  +  str(TXS))
    print ( 'Ethereum Address:  ', ethadd,  '  : TX = ',  str(TXS), '  = Scan Number: ', str(count), '  = Remaining:  ', str(remaining),  end='\r')
    if int(TXS) > 0:
        f=open("ethFound.txt","a")
        f.write('\nPrivate key:'+ priv.to_string().hex())
        f.write('\nAddress:  '+ ethadd)
        f.close()