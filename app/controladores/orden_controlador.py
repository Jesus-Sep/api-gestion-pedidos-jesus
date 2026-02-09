def get_orders():
    return [
        {
            "order_id": 1,
            "status": "pending",
            "total": 250.00
        },
        {
            "order_id": 2,
            "status": "delivered",
            "total": 430.00
        }
    ]
#aqui solo es informacion, no tenemos base de datos asi que tenemos que poner algo
def create_order(order_data: dict):
    return {
        "order_id": 3,
        "status": "pending",
        "total": 300.00,
        "data_received": order_data
    }