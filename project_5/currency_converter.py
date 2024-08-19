import requests

init_currency = input("enter an initial currency : ")
target_currency = input("enter a target currency : ")

while True :
    try:
        amount = float(input("enter the amount : "))
    except:
        print("the amount must be a numeric value! ")
        continue

    if amount == 0:
        print("the amount mist be greater than 0")
        continue
    else:
        break

url = ("https://api.apilayer.com/fixer/convert?to="
        + target_currency + "&from=" + init_currency
        + "&amount=" + str(amount))

payload = {}
headers= {
  "apikey": "SKBxkM2iwivtfTZ2zdJPcycJmveMSRSc"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code

if(status_code != 200):
    print("sorry, there was a problem. please try again later.")
    quit()

result = response.json()
converted_amount = result['result']
print(f'{amount} {init_currency} = {converted_amount} {target_currency}')