orders = []

def create(order_name, status = 'Fabricando'):
    new_order = Order(order_name, status)
    if not input_error:
        orders.append(new_order)

def read(place=''):
    print(f'----ORDERS----{place}')

    for order in orders:
        print(f'ORDER: {order.number}  STATUS: {order.status}')

    print('--------------')

    global has_show
    has_show = True

def update(orders_to_update):
    status = str(input('New status: '))
    if not input_error:
        for order in orders_to_update:
            order_index = getOrderobjectIndexbyNumber(order)
            try:
                if order_index[0] == False:
                    print(f'update: Order {order_index[1]} not found...')
            except:
                orders[order_index].status = status
                

def delete(order_to_delete):
    is_order_number_in_orders = False

    for order in orders:
        if order.number == order_to_delete:
            orders.remove(order)
            is_order_number_in_orders = True

    if is_order_number_in_orders == False:
        print(f'Order {order_to_delete} not found...')

def getOrderobjectIndexbyNumber(number):
    is_in_orders = False

    for order in orders:
        if order.number == number:
            order_index = orders.index(order)
            is_in_orders = True
            return order_index

    if is_in_orders == False:
        return False, number

def getFunctionbyOption(option):
    global input_error
    if option.isalpha():
        option = option[0].lower()
        functions_letters = ['c', 'r', 'u', 'd']

        if option == 'c':
            function = 'create'

        if option == 'r':
            function = 'read'

        if option == 'u':
            function = 'update'

        if option == 'd':
            function = 'delete'

        if option not in functions_letters:
            input_error = True
        else:
            input_error = False

        if not input_error:
            return function
    else:
        input_error = True

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
    global input_error
    if not input_error:
        global has_show
        function = function[0].lower()

        if function != 'r':
            if function == 'c':
                question_core = 'create'
            if function == 'u':
                question_core = 'update'
            if function == 'd':
                question_core = 'delete'

            result = str(input(f'Type the orders to {question_core}: '))
            has_show = False
            input_error = False

        if function == 'r':
            read()
            result = 'read'

        return result

def getOrders(orders_numbers):
    if not input_error:
        # If are not a read method:
        if orders_numbers != 'read':
            orders_numbers = orders_numbers.split(',')

        return orders_numbers

def executeFunction(orders_numbers, function):
    if not input_error:
        # If are a read method:
        if orders_numbers == 'read':
            pass
        else:
            if function == 'create':
                for order in orders_numbers:
                    create(order)

            if function == 'update':
                update(orders_numbers)

            if function == 'delete':
                for order in orders_numbers:
                    delete(order)

class Order:
    def __init__(self, order_number, status='fab'):
        self.number = order_number
        self.status = status

has_show = False
input_error = False

while True:
    #--------------------------------
    if has_show == False:
        read()
    #--------------------------------

    #--------------------------------
    if input_error == False:
        option = str(input('Select an action: CREATE:C READ:R UPDATE:U DELETE:D \n'))
    else:
        option = str(input('Choose an valid option... (CREATE:C READ:R UPDATE:U DELETE:D)\n\n'))

    executeFunction(getOrders(ask(getFunctionbyOption(option))), getFunctionbyOption(option))
    #--------------------------------
