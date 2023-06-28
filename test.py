class Order:
    def __init__(self, order_number, status='fab'):
        self.number = order_number
        self.status = status

orders = []

while True:
    #--------------------------------
    print('----ORDERRS----')
    for order in orders:
        print(f'ORDER: {order.number}  STATUS: {order.status}')
    print('-------------')
    #--------------------------------

    #--------------------------------
    option = str(input('Select an action: CREATE:C READ:R UPDATE:U DELETE:D >>'))
    option = option[0].lower()
    #--------------------------------

    #--------------------------------
    if option == 'c':
        new_order = Order(order_number = str(input('New order number: ')))
        orders.append(new_order)
        
    if option == 'r':
        print('----ORDERS----')
        for order in orders:
            print(f'ORDER: {order.number}  STATUS: {order.status}')
        print('-------------')
        
    if option == 'u':
        order_to_update = str(input('Order to update the status: '))
        new_status = str(input('New status: '))
        for order in orders:
            if order == order_to_update:
                orders[orders.index(order)].status = new_status
            else:
                print(f'Order {order_to_update} not found...')

    if option == 'd':
        old_order = str(input('Order to delete: '))
        for order in orders:
            if old_order == order:
                orders.remove(order)
            else:
                print(f'Order {old_order} not found...')
    #--------------------------------
    #--------------------------------
