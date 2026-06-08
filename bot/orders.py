from bot.logging_config import logger

def place_market_order(symbol, side, quantity):
    logger.info(f"MARKET Order: {side} {quantity} {symbol}")

    return {
        "orderId": "TEST123",
        "status": "FILLED",
        "executedQty": quantity
    }


def place_limit_order(symbol, side, quantity, price):
    logger.info(
        f"LIMIT Order: {side} {quantity} {symbol} at {price}"
    )

    return {
        "orderId": "TEST456",
        "status": "NEW",
        "executedQty": 0
    }