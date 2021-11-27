import requests

url = 'https://panel.uchilecraft.cl/api/client/servers/waterfall/files/upload'
data = {'period': 'monthly', 'interval': '2', 'item[name]': 'test plan', 'item[amount]': '50000', 'item[currency]': 'INR'}
headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': 'Bearer apikey'}
#r = requests.post(url, data=json.dumps(data), headers=headers, auth=('rzp_test_yourTestApiKey', 'yourTestApiSecret'))
r = requests.get(url, headers=headers)
print(r.text)