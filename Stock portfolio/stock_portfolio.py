# ------------------------------------
# Project: Stock Portfolio Tracker
# Internship: CodeAlpha Python Internship
# Developed by: Deep Mishra
# ------------------------------------
# Stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 320,
    "AMZN": 145
}

print("===== Stock Portfolio Tracker =====")

total_value = 0
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    portfolio[stock] = quantity
    total_value += stock_prices[stock] * quantity

print("\nYour Portfolio")

for stock, quantity in portfolio.items():
    print(f"{stock} : {quantity} shares")

print(f"\nTotal Investment Value: ${total_value}")