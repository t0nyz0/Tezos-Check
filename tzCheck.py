import requests
import json
import secret
from datetime import datetime
from dateutil import parser

address = 'tz1UyRLtfQw7vv3EVAgGtSqasfyY4o6fJj8z'

balanceReq  = requests.get(f'https://api.tzkt.io/v1/accounts/{address}/balance')
lastactivityReq  = requests.get(f'https://api.tzkt.io/v1/accounts/{address}/')

result = balanceReq.text

print(f'💳 Address: {address} ')  

def insert_dash(string, index):
  return string[:index] + '.' + string[index:]

balance = insert_dash(result, 4)
lastActive = lastactivityReq.json()
lastActive = lastActive['lastActivityTime']
lastActivityTime = parser.parse(lastActive)
lastActivityTime = lastActivityTime.strftime("%m/%d/%Y, %H:%M:%S")

print(f'💲 Balance: {balance}')
print(f'⌚️ Last update: {lastActivityTime}')


