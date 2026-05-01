from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Request → {symbol} {side} {order_type} qty={quantity} price={price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        logger.info(f"Response → {order}")
        return order

    except Exception as e:
        logger.error(f"Error → {str(e)}")
        raise
