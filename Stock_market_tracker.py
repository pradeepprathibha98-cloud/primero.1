import numpy as np

# Global Price Scaler
prices = np.array([100, 200, 300, 400, 500])

rates = np.array([[0.9],
                  [1.1],
                  [1.5]])
                  
final_table = prices * rates

print("Original Prices:\n", prices)
print("Rates:\n", rates)
print("Final Table:(3 Countries x 5 Products)\n", final_table)
print("Final Table Shape:\n", final_table.shape)

# Stock Market Tracker

stocks = np.array([[150, 155, 160, 165, 170, 175, 180],
                   [200, 190, 180, 170, 160, 150, 140]])

print("Stocks:\n", stocks)

high_prices = stocks[stocks > 170]
print("high_prices:/n", high_prices)

print("Avg per Company:\n", np.mean(stocks, axis = 1))
print("Avg per Day:\n", np.mean(stocks, axis = 0))

crashed_stocks = stocks * 0.8
print("Crashed stocks:\n", crashed_stocks.astype(int))

sales = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print("original sales:\n", sales)
print("Shape of sales:\n", sales.shape)
print("Dinmensions of Sales:\n", sales.ndim)

new_grid = sales.reshape(4, 3)
print("Sales reshaped:\n", new_grid)
print("Shape of new grid:\n", new_grid.shape)

new_month_sales = np.array([[120, 130, 140]])
combined = np.vstack((new_grid, new_month_sales))

print("Combined Sales Grid:\n", combined)
print("Shape of Combined Grid:\n", combined.shape)

top_month_idx = np.argmax(combined)
print("Index of top monthly sales:\n", top_month_idx)

