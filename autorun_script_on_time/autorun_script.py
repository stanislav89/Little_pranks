import schedule
import requests


def bitcoin_rate():
    response = requests.get(url='https://yobit.net/api/3/ticker/btc_usd')
    data = response.json()
    btc_price = f"BTC: {round(data.get('btc_usd').get('last'), 2)}$\n"
    print(btc_price)


def main():
    schedule.every(5).seconds.do(bitcoin_rate)
    schedule.every(1).minute.do(bitcoin_rate)
    schedule.every(1).hour.do(bitcoin_rate)
    schedule.every().day.at('22:00').do(bitcoin_rate)
    schedule.every().friday.at('23:00').do(bitcoin_rate)

    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main()
