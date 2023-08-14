def delete_not_numbers(list):
    
    counter_not_number = 0

    for item in list:
        if item.isnumeric() == False:
            counter_not_number += 1

    for i in range(counter_not_number):
        for item in list:
            if item.isnumeric() == False:
                list.remove(item)

    new_list = list

    return new_list