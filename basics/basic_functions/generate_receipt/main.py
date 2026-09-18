def generate_receipt(customer_name, items, discount = 0, delivery_fee = 4.99):
    total_items = count_items(items)
    item_price = 2.50
    subtotal = total_items * item_price

    discount_amount = subtotal * (discount / 100)
    subtotal_after_discount = subtotal - discount_amount

    final_total = subtotal_after_discount + delivery_fee

    receipt = (
        f"Customer: {customer_name}\n"
        f"Items: {items}\n"
        f"Number of items: {total_items}\n"
        f"Subtotal: £{subtotal:.2f}\n"
        f"Discount: {discount}% (-£{discount_amount:.2f})\n"
        f"Delivery fee: £{delivery_fee:.2f}\n"
        f"Total: £{final_total:.2f}"
    )

    return receipt
    
def count_items(list_of_items):
    count = 0
    for i in list_of_items:
        count += 1
    return count

print(generate_receipt("Aamer", ["Milk", "Bread"], discount=20, delivery_fee=2.99))
