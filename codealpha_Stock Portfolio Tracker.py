# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("=== STOCK PORTFOLIO TRACKER ===")

# Number of stocks user wants to enter
n = int(input("How many stocks do you own? "))

for i in range(n):

    stock_name = input("Enter stock name: ").upper()

    quantity = int(input("Enter quantity: "))

    # Check if stock exists
    if stock_name in stock_prices:

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print("Investment in", stock_name, "=", investment)

    else:
        print("Stock not found.")

print("\nTotal Investment Value =", total_investment)