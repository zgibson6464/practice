class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:
    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        self.customer = customer
        self.flavor = flavor
        self.scoops = scoops
        order = {
            'Customer:': customer,
            'Flavor:': flavor,
            'Scoops:': scoops}

        if flavor not in self.flavors:
            print('Invalid flavor')
            return
        if scoops not in range(1, 4):
            print('invalid amount of scoops, choose 1, 2, or 3')
            return
        else:
            print('Order created!')
            self.orders.enqueue(order)

    def show_all_orders(self):
        print()
        print('All Pending Ice Cream Orders:')
        for item in self.orders.items:
            print(
                f'Customer: {item.get("Customer:")} -- Flavor: {item.get("Flavor:")} -- Scoops: {item.get("Scoops:")}')

    def next_order(self):
        order = self.orders.dequeue()
        print()
        print('Next Order Up!')
        print(
            f'Customer: {order.get("Customer:")} -- Flavor: {order.get("Flavor:")} -- Scoops: {order.get("Scoops:")}')


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 3)
shop.take_order("Marcy", "mint chip", 1)
shop.take_order("Leopold", "vanilla", 2)
shop.take_order("Bruce", "rocky road", 0)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
