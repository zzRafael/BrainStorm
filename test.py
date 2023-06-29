orders = []

def create(order_name, status = 'Fabricando'):
    new_order = Order(order_name, status)
    orders.append(new_order)
    
def read():
    print('----ORDERS----')
    for order in orders:
        print(f'ORDER: {order.number}  STATUS: {order.status}')
    print('--------------')
    
def update():
    order_number = str(input('Order to update the status: '))
    new_status = str(input('New status: '))
    is_order_number_in_orders = False
    for order in orders:
        if order.number == order_number:
            orders[orders.index(order)].status = new_status
            is_order_number_in_orders = True
    if is_order_number_in_orders == False:
            print(f'Order {order_number} not found...')
            
def delete():
    order_to_delete = str(input('Order to delete: '))
    is_order_number_in_orders = False
    for order in orders:
        if order.number == order_to_delete:
            orders.remove(order)
            is_order_number_in_orders = True
    if is_order_number_in_orders == False:
        print(f'Order {order_to_delete} not found...')

def getFunctionbyOption(option):
    option = option[0].lower()
    if option == 'c':
        function = 'create'
    if option == 'r':
        function = 'read'
    if option == 'u':
        function = 'update'
    if option == 'd':
        function = 'delete'
    return function

def getStatusbyOption(option):
    option = option[0].lower()
    if option == 'c':
        status = 'create'
    if option == 'r':
        status = 'read'
    if option == 'u':
        status = 'update'
    if option == 'd':
        status = 'delete'
    return status

def ask(function):
    function = function[0].lower()
    if function == 'c':
        question_core = 'create'
    if function == 'u':
        question_core = 'update'
    if function == 'd':
        question_core = 'delete'
    result = str(input(f'Type the orders to {question_core}: '))
    return result
    
def getOrders(orders_numbers):
    orders_numbers = orders_numbers.split(',')
    return orders_numbers
    
def executeFunction(orders_numbers, function = 'c'):
    function = getFunctionbyOption(function)
    if function == 'create':
        for order in orders_numbers:
            create(order)
    if function == 'update':
        for order in orders_numbers:
            pass
    if function == 'delete':
        for order in orders_numbers:
            pass

class Order:
    def __init__(self, order_number, status='fab'):
        self.number = order_number
        self.status = status

'''executeFunction(getOrders(), function = 'c')
read()'''

while True:
    #--------------------------------
    read()
    #--------------------------------

    #--------------------------------
    option = str(input('Select an action: CREATE:C READ:R UPDATE:U DELETE:D >>'))

    executeFunction(getOrders(ask(getFunctionbyOption(option))), getFunctionbyOption(option))
    
    
    #--------------------------------
