import requests, sys

def main():

    if len(sys.argv) == 1:
        print("Missing command-line argument")
        sys.exit(1)
    elif not (sys.argv[1].isnumeric() or is_float(sys.argv[1])):
        print("Command-line argument is not a number")
        sys.exit(1)
    totalPrice = float(fetch_price()) * float(sys.argv[1])
    print(f"${totalPrice:,.4f}")



def fetch_price():
    try:
        response = requests.get(' https://api.coindesk.com/v1/bpi/currentprice.json')
        jsonInfo = response.json()
        ##jsonInfo>>bpi>>rate_float
        ##for result in jsonInfo['bpi']:
          ##  print(result)
        bitcoinRate = jsonInfo['bpi']['USD']['rate_float']
        return bitcoinRate

    except requests.RequestException:
        pass

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
main()
