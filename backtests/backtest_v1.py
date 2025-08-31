def run_moving_average_backtest(price_data, short_window=3, long_window=5):
    if len(price_data) < long_window:
        print("Not enough data to perform backtest.")
        return 1000
    
    portfolio_value = 1000
    is_holding_asset = False
    
    print(f"Starting backtesting with an initial portfolio of ${portfolio_value}")
    
    for i in range(long_window, len(price_data)):
        short_ma = sum(price_data[i - short_window:i]) / short_window
        long_ma = sum(price_data[i - long_window:i]) / long_window
        
        if short_ma > long_ma and not is_holding_asset:
            print(f"Buy signal on day {i}, current price is ${price_data[i]}")
            is_holding_asset = True
        
        elif short_ma < long_ma and is_holding_asset:
            print(f"Sell signal on day {i}, current price is ${price_data[i]}")
            is_holding_asset = False
    
    if is_holding_asset:
        final_price = price_data[-1]
        print(f"Backtest finished. Still holding asset at final price of ${final_price}")
        return portfolio_value
    
    print("Backtest finished. Not holding asset.")
    return portfolio_value

if __name__ == '__main__':
    sample_prices = [10, 11, 12, 11, 10, 11, 12, 13, 14, 15, 14, 13]
    final_value = run_moving_average_backtest(sample_prices)
    print(f"Final portfolio value: ${final_value}")
