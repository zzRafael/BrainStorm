from random import choice

def prob(dic, times):
    #probabilidades iniciais
    dic = dic

    #criando uma lista com x% de numeros para cada item(não pode passa de 100)
    itens_dic = []
    for i in dic:
        itens_dic.append(i)
    #print(itens_dic)
    list_with_porcentage = []
    for quant in itens_dic:
        for i in range(quant):
            list_with_porcentage.append(dic[quant])
    #mostrando na telo a quantidade de cada item na list_with_porcentage
    #print(list_with_porcentage)
    for i in dic:
        num = list_with_porcentage.count(dic[i])
        #print(f'{dic[i]}: {num}')

    #Selecionando os numeros pela probabilidade(test. Pode ser com o que quiser) e colocando em uma lista
    list = []
    for i in range(times):
        choose = choice(list_with_porcentage)
        list.append(choose)
    #contando quantos elementos de cada item na lista list
    list_return = []
    for i in dic:
        num = list.count(dic[i])
        #print(f'{dic[i]}: {num}')
        list_return.append(f'{dic[i]}: {num}')
    #print(list_with_porcentage)
    return choice(list_with_porcentage)

class Planet:
    def __init__(self, name, size, type, habit):
        self.size = size
        self.type = type
        self.name = name
        self.habit = habit
        #Como o tamanho do planeta será mostrado na frase
        if self.size == 'Small':
            in_frase_size = 'um pequeno planeta'
        elif self.size == 'Medium':
            in_frase_size = 'um planeta médio'
        elif self.size == 'Big':
            in_frase_size = 'um grande planeta'
        elif self.size == 'Anão':
            in_frase_size = 'um planeta anão'
        #Como o tipo do planeta será mostrado na frase
        if self.type == 'aquatic':
            in_frase_type = 'aquático'
        if self.type == 'desertic':
            in_frase_type = 'desértico'
        if self.type == 'gas':
            in_frase_type = 'gasoso'
        if self.type == 'frozen':
            in_frase_type = 'congelado'
        if self.type == 'tempered':
            in_frase_type = 'temperado'
        #como a habitabilidade será mostrada na frase
        if self.habit == 'Inabitável':
            in_frase_habit = 'Condições desfavoráveis para abrigar vida.'
        if self.habit == 'Habitável':
            in_frase_habit = 'Este planeta possui condições favoraveis a vida!!!.'
        #mostrando a frase de informação
        print(f'O planeta {self.name} é {in_frase_size} do tipo {in_frase_type}. {in_frase_habit}')

def createPlanets(quant):
    for i in range(quant):
        #quão precisa serão as probabilidades
        times = 100
        #coloque em dicionario a porcentagem e o item: {20:'Sim', '80','Não'})
        planet_names_file = open('planets_names.txt')
        names = planet_names_file.readlines()
        size_prob = {20:'Medium', 30:'Small', 19:'Big', 21:'Anão'}
        type_prob = {2:'aquatic', 29:'gas', 35:'frozen', 31:'desertic', 3:'tempered'}
        habit_prob = {10:'Habitável', 90:'Inabitável'}
        name = choice(names).replace('\n', '')
        size = prob(size_prob, times)
        #impedindo criação de planetas improváveis
        #tamanho
        if size == 'Anão':
            type_prob = {2:'aquatic', 49:'frozen', 48:'desertic'}
            habit_prob = {1:'Habitável', 99:'Inabitável'}
        if size == 'Small':
            type_prob = {2:'aquatic', 35:'frozen', 31:'desertic', 3:'tempered'}
            habit_prob = {5:'Habitável', 200:'Inabitável'}
        if size == 'Medium':
             habit_prob = {10:'Habitável', 85:'Inabitável'}
        if size == 'Big':
            type_prob = {2:'aquatic', 60:'gas', 20:'frozen', 20:'desertic', 3:'tempered'}
        type = prob(type_prob, times)
        #deixando as probabilidades abrigar vida mais realistas
        #tipo
        if type == 'aquatic':
            habit_prob = {50:'Habitável', 49:'Inabitável'}
        if type == 'gas':
            habit_prob = { 100:'Inabitável'}
        if size == 'Medium' and type == 'tempered':
            habit_prob = {51:'Habitável', 49:'Inabitável'}
        habit = prob(habit_prob, times)

        planet = Planet(name, size, type, habit)