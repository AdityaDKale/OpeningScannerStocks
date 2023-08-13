# Importing Libraries

from os import remove
import datetime
from pandas import read_csv, DataFrame, merge
from requests import get

# Getting Pre-Open Data with cookies from nseindia
try:
    print("Getting Pre-open Value from NSE..")
    h1 = {"Host": "www.nseindia.com",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept":
              "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
              "Referer": r"https://www.nseindia.com/market-data/pre-open-market-cm-and-emerge-market"
          }

    r = get(h1["Referer"], headers=h1).cookies
    query = r'https://www.nseindia.com/api/market-data-pre-open?key=NIFTY&csv=true'
    a = get(query, headers=h1, cookies=r)
except:
    print("Unable to get preopen data from NSE")

# Creating a Temporary txt file
print("")
print("Creating Temporary file..")
with open('tempFile.txt', 'w') as f:
    f.write(str(a.text))
print("Loading Pre-open Data")
try:
    db = read_csv("tempFile.txt")
except:
    print("Unable to load pre-open data into csv")
print("Removing temp file")
remove('tempFile.txt')

print("Loading Pre-open Database")
print("Creating Symbols..")

# Creating Pre-Open database

SYMBOLS = db.iloc[:, 0].to_list()
print("Extracting Pre-open value")
PREOPENVALUE = db.iloc[:, 5].to_list()
PREOPEN = []
print("Inserting preopen value into database..")
for i in range(50):
    preOpen = PREOPENVALUE[i].replace(',', "")
    preOpen = float(preOpen)
    PREOPEN.insert(i, round(preOpen, 2))
db1 = DataFrame({'Symbols': SYMBOLS, 'Pre-Open': PREOPEN})
print("")
print("Pre-open data loaded successfully.")
# print(db1)
print("")
print("Getting equity data from NSE..")
try:
    h1 = {"Host": "www.nseindia.com",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept":
          "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
          "Referer": r"https://www.nseindia.com/market-data/live-equity-market?symbol=NIFTY%2050"
          }

    r = get(h1["Referer"], headers=h1).cookies
    query = r'https://www.nseindia.com/api/equity-stockIndices?csv=true&index=NIFTY 50'
    a = get(query, headers=h1, cookies=r)
except:
    print("Unable to get OHLC data from NSE")

# Creating a Temporary txt file
print("Creating temp file..")
with open('tempFile.txt', 'w') as f:
    f.write(str(a.text))
print("Loading OHLC data..")
db = read_csv("tempFile.txt")
print("Removing Temp file..")
remove('tempFile.txt')

print("Creating OHLC database..")
print("Loading Symbols..")

SYMBOLS1 = db.iloc[:, 0].to_list()
print("Extracting OHLC data..")
OPEN = db.iloc[:, 1].to_list()
HIGH = db.iloc[:, 2].to_list()
LOW = db.iloc[:, 3].to_list()
CLOSE = db.iloc[:, 5].to_list()
PIVOT = []
R1 = []
S1 = []
print("Calculating pivot ranges..")
for i in range(51):
    o = OPEN[i].replace(',', "")
    h = HIGH[i].replace(',', "")
    l = LOW[i].replace(',', "")
    c = CLOSE[i].replace(',', "")
    pp = (float(h)+float(l)+float(c))/3
    r1 = pp + ((float(h)-float(l))*0.382)
    s1 = pp - ((float(h)-float(l))*0.382)
    PIVOT.insert(i, round(pp, 2))
    R1.insert(i, round(r1, 2))
    S1.insert(i, round(s1, 2))
print("Inserting data into database")
db2 = DataFrame({"Symbols": SYMBOLS1, "Open": OPEN,
                 "High": HIGH, "Low": LOW, "Close": CLOSE, "Pivot": PIVOT, "R1": R1, "S1": S1})
db2.drop(0, axis=0, inplace=True)
db2 = db2.reset_index(drop=True)
# db2.insert(-1, "Pivot", PIVOT, True)
# print(db2)
print("")
print("Successfully loaded OHLC data.")
print("")
print("Merging database")
db3 = merge(db2, db1, on=["Symbols"])
GREATERTHANR1 = []
LESSTHANS1 = []
print("Checking conditions..")
db3['Greater than R1'] = (db3['Pre-Open'] >= db3['R1'])
db3['Less than S1'] = (db3['Pre-Open'] <= db3['S1'])
print("Conditions checked successfully..")
print("")
print("Creating excel file")
today = datetime.date.today()
db3.to_excel(f'{today} - Opening Scanner.xlsx', index=False)
print(db3)
input("Press enter to exit.. ")
