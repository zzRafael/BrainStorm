import mysql.connector
from faker import Faker
from random import choice, randint

# defining faker
locales = 'pt-BR'
fk = Faker(locales)
black_list_names = ['Dra.', 'Sra.', 'Dr.', 'Sr.', 'da', 'do', 'de', 'Srta.']

# define models
models = ['China 3mm', 'Capadócia 4mm', 'Slim 2mm', 'Classic 2mm', 'Noruega 3mm', 'Florenza 5mm', 'Twist 2mm', 'Chanfrada 2mm']

# database connection
con = mysql.connector.connect(host='localhost', database='fakeinfos', user='root', password='')

# define cursor
cursor = con.cursor()

# checking for the connection
if con.is_connected():
    print('Connection established!')
    for i in range(3225):
        # generate the fake infos
        # fake name
        fake_name = fk.name()
        fake_name = fake_name.split(' ')
        if fake_name[0] in black_list_names:
            fake_name = f'{fake_name[1]}'
        else:
            fake_name = f'{fake_name[0]}'
        # fake cpf
        fake_cpf = randint(10000000000,99999999999)
        # fake model
        fake_model = choice(models)

        # define a command
        command = f'INSERT INTO fake_people(first_name, CPF, models) VALUES ("{fake_name}", {fake_cpf}, "{fake_model}");'
        cursor.execute(command)

# save and close
con.commit()
cursor.close()
con.close()
