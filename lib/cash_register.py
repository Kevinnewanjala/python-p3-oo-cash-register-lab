class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.previous_transactions = []  
        
    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity) 
        self.previous_transactions.append({"title": title, "price": price, "quantity": quantity})  # Record the transaction
        return self.items
        
    def apply_discount(self):
        if self.discount:
            self.total = int(self.total * ((100 - self.discount) / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")
            
    def void_last_transaction(self):
        if not self.previous_transactions:
            return "There are no transactions to void."
        last_transaction = self.previous_transactions.pop()
        last_price = last_transaction["price"]
        last_quantity = last_transaction["quantity"]
        self.total -= last_price * last_quantity
        # Remove the last item(s) from the items list
        for _ in range(last_quantity):
            self.items.pop()
        return f"The last transaction (${last_price} each, {last_quantity} items) has been voided."
