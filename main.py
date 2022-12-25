import ccxt
import time

exchange_one = ccxt.binance()
exchange_two = ccxt.kucoin()


def main():
    price_ex_binance = exchange_one.fetch_ticker('BTC/USDT')['last']
    price_ex_kucoin = exchange_one.fetch_ticker('BTC/USDT')['last']

    arbitrage = price_ex_kucoin - price_ex_binance

    if arbitrage > 0:
        print('arbitrage detected')

        # buy on ex binance
        amount_to_buy = 10
        purchase_on_exchange_binance = exchange_one.create_market_buy_order('BTC/USDT', amount_to_buy)

        # sell on ex kucoin

        amount_to_sell = purchase_on_exchange_binance['amount']
        sell_on_exchange_kucoin = exchange_two.create_limit_sell_order('BTC/USDT', amount_to_sell)
    else:
        print(f'binance {price_ex_binance} --- kucoin {price_ex_kucoin}')

    time.sleep(2)


while True:
    main()
