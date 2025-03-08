def main():
    balance = 50
    print("Amount Due:", balance)

    while balance > 0:
        coins = int(input("Insert Coin: "))
        if iscorrect(coins):
            balance -= coins
        if balance > 0:
            print("Amount Due:",balance)


    print("Change Owed:", str(abs(balance)).strip())



def iscorrect(coin):
    if coin == 25 or coin == 10 or coin == 5:
        return True


main()
