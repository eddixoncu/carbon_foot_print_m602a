print('Welcome Advanced programming')


class Item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


def get_available_items():
    items = [Item("Razor", 50), Item("Balm", 20), Item("Brush", 15)]

    return items


def get_shop_cart(items, razors, balms, brushes):
    shop_cart = {}
    for item in items:
        if item.name == "Razor":
            shop_cart[item.name] = [item.price, razors]
        elif item.name == "Balm":
            shop_cart[item.name] = [item.price, balms]
        elif item.name == "Brush":
            shop_cart[item.name] = [item.price, brushes]
    return shop_cart

def print_shop_cart(shop_cart:{}):
    total = 0.0
    for item in shop_cart:
        print(f'{item}\tunit price {shop_cart[item][0]}\tquantity {shop_cart[item][1]}\tsub total {shop_cart[item][0]*shop_cart[item][1]}')
        total += shop_cart[item][0]*shop_cart[item][1]

    print(f"TOTAL : {total}")


def main():
    items = get_available_items()
    idx = 1
    for item in items:
        print(f'{idx}\titem {item.name} \tprice {item.price} ')
        idx += 1

    qty_razors = int(input("Enter number of razors to buy "))
    qty_balm = int(input("Enter number of balm to buy "))
    qty_brushes = int(input("Enter number of brushes to buy "))

    cart = get_shop_cart(items, qty_razors, qty_balm, qty_brushes)
    print_shop_cart(cart)

    

if __name__ == "__main__":
    main()
