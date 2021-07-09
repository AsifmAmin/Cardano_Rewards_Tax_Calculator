# Cardano_Rewards_Tax_Calculator



# Calculator

➕ A simple calculator made in python.



## 🛠 Getting started

Windows:

You can clone the repository through CMD (Command Prompt) just by typing:

```sh
git clone https://github.com/AsifmAmin/Cardano_Rewards_Tax_Calculator
```

or download the zip from the green button at the beginning of the repository

<img src="https://i.imgur.com/M2YvvGp.png" alt="Download zip" border="0" width="350">

<img src="https://i.imgur.com/NEeFHRg.png" alt="Download zip" border="0" width="350">

## 📄 Neccessary files needed to run the program

1. Go to <https://www.cryptodatadownload.com/data> scroll down and choose between Binance or Kucoin,
and download ADA/USDT minute version. Save the CSV file into the projects folder
<img src="https://i.imgur.com/QEFINhu.gif"  border="0" width="800">
   
   <br>
   
2. Find your <a href="https://i.imgur.com/ZKrUdyX.png">wallet address</a> and go to <https://pooltool.io/> and enter your address in this search bar<br>

<img src="https://i.imgur.com/JfsJL2V.gif"  border="0" width="900">

Scroll down to **Export Tool** and choose *Format* CoinTracking.info (CSV), for *Currency* choose US Dollar,
and for *Periode* you could choose for the year you want to calculate for. Then save this CSV file into the 
projects folder 

## 💻 How to run the program 

1. Download all the requirements by writing this in terminal ``` pip install -r requirements.txt ```

2. run the python script, it is going to ask you to select your <a href="https://i.imgur.com/t9TOofh.png"> reward file</a>
which you got from pooltool.io, then it is going to ask you for the *ADA/USDT CSV file*.

3. Now it is going to ask you for
which currency you want it displayed as, you could choose between 166 currencies, you need to write the input as: ***USD, SEK, NOK, CAD*** etc
   <a href="https://github.com/fawazahmed0/currency-api/blob/1/latest/currencies.json">[CHECK HERE FOR SUPPORTED CURRENCIES]    
</a> 

4. Now you need to find how much your country tax for each reward, for instance in norway they tax 22% for each reward we get, 
so here i would write 0.22. 
   ![](https://i.imgur.com/UQEeG57.png)
5. Now the script is going to calculate how much you need to tax for each reward, and put it into a CSV file ***:)*** 

## 🚀 Contribution

1. Make the _fork_ of the project (<https://github.com/AsifmAmin/Cardano_Rewards_Tax_Calculator/fork>)
2. Create a _branch_ for your modification (`git checkout -b my-new-resource`)
3. Do _commit_ (`git commit -am 'Adding a new resource ...'`)
4. _Push_ (`git push origin my-new-feature`)
5. Create a new _Pull Request_

**After your pull request is merged**, you can safely delete your branch.


---