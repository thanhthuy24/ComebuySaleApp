def count_cart(cart):
    total_amount, total_quantity = 0, 0

    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += float(c['quantity'])*float(c['price'])

    return {
        "total_amount": total_amount,
        "total_quantity": total_quantity

    }