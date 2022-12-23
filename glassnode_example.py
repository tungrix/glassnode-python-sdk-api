from glassnode_util import GlassnodeConsumer, load_config


if __name__ == "__main__":
    api_key = load_config(filename="config.json", key="api_key")

    glassnode_consumer = GlassnodeConsumer(api_key=api_key)

    # get all closing price data of bitcoin (earliest from 2010-07-17)
    df = glassnode_consumer.get_close_price(symbol='BTC')
    print(df)

    # get specific interval of bitcoin closing price
    df = glassnode_consumer.get_close_price(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01')
    print(df)

    # get specific interval with specific timeframe of bitcoin closing price
    df = glassnode_consumer.get_close_price(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01', interval='1h')
    print(df)

    # get ohlc data
    df = glassnode_consumer.get_ohlc(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01', interval='24h')
    print(df)

    # get issuance data
    df = glassnode_consumer.get_issuance(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01', interval='24h')
    print(df)

    # get inflation rate data
    df = glassnode_consumer.get_inflation_rate(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01',
                                               interval='24h')
    print(df)

    # get puell multiple data
    df = glassnode_consumer.get_puell_multiple(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01',
                                               interval='24h')
    print(df)

    # get total fees data
    df = glassnode_consumer.get_total_fees(symbol='BTC', from_date='2020-01-01', to_date='2021-01-01', interval='24h')
    print(df)

    # get exchange netflow
    df = glassnode_consumer.get_exchange_netflow(symbol='BTC', from_date='2022-01-01', to_date='2023-12-24', interval='24h')
    print(df)

