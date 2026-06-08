from bot.validators import validate_order
from bot.orders import place_market_order, place_limit_order

try:
    print("===== Binance Trading Bot =====")

    symbol = input("Enter Symbol (BTCUSDT): ").upper()
    side = input("Enter Side (BUY/SELL): ").upper()
    order_type = input("Enter Order Type (MARKET/LIMIT): ").upper()

    quantity = float(input("Enter Quantity: "))

    price = None

    if order_type == "LIMIT":
        price = float(input("Enter Price: "))

    validate_order(
        symbol,
        side,
        order_type,
        quantity,
        price
    )

    if order_type == "MARKET":
        result = place_market_order(
            symbol,
            side,
            quantity
        )
    else:
        result = place_limit_order(
            symbol,
            side,
            quantity,
            price
        )

    print("\n===== ORDER RESPONSE =====")
    print("Order ID:", result["orderId"])
    print("Status:", result["status"])
    print("Executed Qty:", result["executedQty"])

except Exception as e:
    print("Error:", e)