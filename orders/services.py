import requests

def generate_payment_link(order):
    # Replace with the real payment gateway API
    payment_gateway_url = "https://payment-gateway.example.com/api/payment-link"
    response = requests.post(payment_gateway_url, json={
        "amount": float(order.total_price),
        "currency": "USD",
        "redirect_url": "https://your-domain.com/payment-success/",
        "metadata": {
            "order_id": order.id
        }
    })

    if response.status_code == 201:
        return response.json().get("payment_link")
    return None
