from collections import Counter

Price = {"Soap":50,"ToothPaste":25,"Shampoo":45.50,"ToothBrush":15.99}

Cart = Counter(Soap=5, ToothPaste=1, Shampoo=2, ToothBrush=3)

def generate_bill(price,cart):
    print(f"Product        Price  Qty  Sub-total")
    total = 0
    for pri in price:
        if pri in cart:    # {pri : 10}, where :10 if for formating , giving space in terms of columns.
            print(f"{pri:10} : {price[pri]:5} X {cart[pri]:3} = {price[pri] * cart[pri]:5} ")
            total += (price[pri] * cart[pri])
    print(f"Total =                  = {total}")

generate_bill(Price,Cart)

