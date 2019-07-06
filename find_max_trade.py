# Given a list of stock prices for a company, find the maximum amount of money you could have made with one trade (one buy/sell). 
# For example, if A = [2,3,1,4,5,7,5,4], the max money with a single trade is 6, if you buy at 1 and sell at 7.


def get_max_trade(trade_list):
    min_value_sofar = float('inf')
    max_trade = 0
    
    for i in range(len(trade_list)):
        min_value_sofar = min(trade_list[i], min_value_sofar)
        max_trade_at_i = trade_list[i] - min_value_sofar
        max_trade = max(max_trade, max_trade_at_i)
        
    return max_trade
    
print(get_max_trade([8,12,9,10,50,60,2]))

