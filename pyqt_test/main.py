def create(id):
    list.append(id)

def read(id):
    print(id)

def update(id, new_id):
    list.remove(id)
    list.append(new_id)

def delete(id):
    try:
        for i in range(len(list)):
            list.remove(id)
    except ValueError:
        pass

title = 'System'
char = '='
char_num = 10

list = []

print(char * char_num,' System ', char * char_num)

while True:
    option = input('Escolha uma opção: c=criar, r=ler, u=atualizar, d=deletar, s=sair: ')
    if option[0] == 'c':
        created_id = input('Informe o novo ID para cadastro: ')
        create(created_id)

    if option[0] == 'r':
        print("======List======")
        if len(list) < 1:
          print('A lista está vazia. Digite "c" para adicionar mais IDs.')
        else:
            for item in list:
                print(item)
        print("======List======")

    if option[0] == 'u':
        old_id = input('Informe a ANTIGO ID: ')
        new_id = input('Informe a NOVO ID: ')
        update(old_id, new_id)

    if option[0] == 'd':
        to_delete = input('Digite o ID que deseja deletar: ')
        delete(to_delete)
    
    if option[0] == 's':
        break


print(char * char_num,' System foi fechado ', char * char_num)