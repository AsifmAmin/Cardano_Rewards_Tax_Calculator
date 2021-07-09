import pandas as pd

import requests
from tkinter import *
from tkinter.filedialog import askopenfilename

pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)
Tk().withdraw()  # removing the small tk GUI window



# https://pooltool.io/address
# add your reward file
print("Choose your reward CSV from pooltool.io")
DFrewards = pd.read_csv(askopenfilename())

# https://www.cryptodatadownload.com/
print("Select your price history CSV file ")
DFprice_history = pd.read_csv(askopenfilename(),low_memory=False, # add binance/kucoin CSV file here
                              skiprows=1)  # https://www.cryptodatadownload.com/

whichCurr= input("Write your country valuta symbol name, example, eur, usd ")



# Renaming the columns name, so it would be more accurate
DFprice_history = DFprice_history.rename(columns={'open':'ADA Price'},inplace=False) # add binance/kucoin CSV file here
DFrewards = DFrewards.rename(columns={'Date':'date'},inplace=False)

DFrewards = DFrewards.dropna(axis=1)  # Dropping all NaN columns
dropColumn = ['tradecount'] # if this/these columns exits then drop them, only
# Binance provides tradecount, and not kucoin.

for col in dropColumn:
    if col in DFprice_history.columns:
        DFprice_history = DFprice_history.drop(columns=dropColumn, axis=1)


# removing everything starting from "Stake" and above.
remchar = 'Stake'
DFrewards['Comment'] = DFrewards['Comment'].map(lambda x:str(x).split(remchar,1)[0])

DFrewards['Comment'] = DFrewards['Comment'].values[::-1]  # making in it correct order

# dropping unecessarry columns/years
DFprice_history = DFprice_history.drop(
    ['unix','symbol','high','low','close','Volume ADA','Volume USDT'],axis=1)

DFprice_history = DFprice_history[DFprice_history['date'].str.contains("2020")==False]

# Changing the order from yyyy-mm-dd to dd-mm-yyyy
date_old = pd.to_datetime(DFrewards["date"])
change_format = date_old.dt.strftime('%Y-%m-%d %H:%M:00')

# merging both of the df, and ending up with the date and the how much ADA wash worth that moment
dataframe_df = pd.merge(DFprice_history,change_format,on=['date'],how='inner')

dataframe_df["Rewards"] = DFrewards['Buy'].values[::-1]  # adding in the correct order(reversed)

dataframe_df.insert(0,"Epoch",DFrewards['Comment'],True)  # inserting epoch data into the first column

# adding two new columns, one for how much usd you got, and second how much you need to tax of it
dataframe_df['Total USD $'] = dataframe_df['ADA Price']*dataframe_df['Rewards']
PrecentageToTax = float(input("Write how much you need to tax for cardano rewards. "))
dataframe_df['How much to tax in USD '] = dataframe_df['Total USD $'] * 0.22

# removing seconds from date to match with the URL
remchar = ' '
dataframe_df['date'] = dataframe_df['date'].map(lambda x:str(x).split(remchar,1)[0])
dictdata = (dataframe_df['date'].to_dict())

repons = []


#Where i am getting currency API from https://github.com/fawazahmed0/currency-api
for key in dictdata.values():
    url = requests.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/" + key + "/currencies/usd.json")

    data_dict = url.json()  # data to dict
    repons.append(data_dict)  # adding data to the list

custom_curr = []

# storing the correct currency inside a list which is going to be added to the DF
for i in range(len(repons)):
    repons[i][i] = repons[i]['usd']
    custom_curr.append(repons[i][i][whichCurr])


dataframe_df['Valuta: ' + whichCurr.upper()] = custom_curr #adding users currency to the data frame

dataframe_df['Total in ' + whichCurr.upper()] = dataframe_df['Total USD $'] * dataframe_df['Valuta: ' + whichCurr.upper()] # total earned in user currency

dataframe_df['How much to tax in ' + whichCurr.upper()] = dataframe_df['How much to tax in USD ']  * dataframe_df['Valuta: ' + whichCurr.upper()] # how much to tax in users currency

dataframe_df.to_csv('Report_Tax_Rewards.csv',sep=';')
print(dataframe_df)

