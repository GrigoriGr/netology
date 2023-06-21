# # print(type('hello world'))

# # class Character: # создали класс 'Character'
# #     pass

# # peter = Character() # создали экземпляр класса
# # print(type(peter))

# # добавим классу атрибутов
# class Character: 
#     name = 'some name'
#     power = 0
#     energy = 100
#     hands = 2

# # при вызвое класса мы всегда создаём новый объект 
# # у конкретного экземпляра будут все теже атрибуты, что и у его класса
# peter = Character()
# print(peter.name)
# print(peter.power)
# print(peter.energy)
# print(peter.hands)

# # мы можем экземпляру присвоить свои атрибуты
# peter.name = 'Peter Parker'
# peter.power = 70
# # и даже те, которых изначально нет в самом классе
# peter.alias = 'Spider-Man' # type: ignore
# print(peter.alias) # type: ignore


# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85
# bruce.alias = 'Batman'

# print(bruce.name)
# print(bruce.power)
# print(bruce.energy)
# print(bruce.hands)
# print(bruce.alias)


# придумаем несколько методов для нашего класса 
# class Character: 
#     name = 'some name'
#     power = 0
#     energy = 100
#     hands = 2

#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')

#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
    
#     def change_alias(self, new_alias):
#         print(self)
#         self.alias = new_alias

# # еще раз проиницаилизируем создание экземпляра
# bruce = Character()
# bruce.name = 'Bruce Wayne'
# bruce.power = 85

# bruce.change_alias('Dark knight')
# print(bruce.alias)

# class Character:
#     name = 'some_name'
#     power = 0
#     energy = 0
#     hands = 2
#     backpack = [] # добавляем атрибут с изменяемым типом – списком
    
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
        
    
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
    
#     def change_alias(self, new_alias):
#         self.alias = new_alias


# peter = Character()
# bruce = Character()

# peter.backpack.append('web-shooters') # дадим Питеру веб-шутеры

# print(peter.backpack)


# # а что с Бэтманом?
# print(bruce.backpack)




# class Character:
#     var = 5
    
#     def __init__(self, name, power, energy=100, hands=2):
#         # параметром по-умолчанию backpack делать не будем, чтобы он не был общим
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = [] # будем присваивать пустой список именно для КОНКРЕТНОГО экземпляра при создании (self)
#         self.hands = hands

#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')        
    
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
    
#     def change_alias(self, new_alias):
#         self.alias = new_alias

# теперь при создании экземпляра класса нам надо обязательно передать аргументы
# peter = Character()
# peter = Character('Peter Parker', 80, hands=6)
# bruce = Character('Bruce Wayne', 85)
# print(peter.name)
# print(peter.power)
#если они не заданы по умолчанию
# print(peter.hands)

# плюс мы решим проблемы общих изменяемых атрибутов
# peter.backpack.append('web-shooters')

# print(peter.backpack)
# print(bruce.backpack)


# Итого: в init будем прописывать то, что хотим задавать при инициализации экзмепляров класса. Все атрибуты с изменямыми значениями по-умолчанию, которые по плану будут общие для всех экзмепляров можно прописывать без него

# Взаимодействия классов: посмотрим на основе сложения


# class Character:
#     '''
#     class doscstring
#     '''
#     def __init__(self, name, power, energy=100, hands=2):
#         self.name = name
#         self.power = power
#         self.energy = energy
#         self.backpack = []
#         self.hands = hands
    
#     def eat(self, food):
#         if self.energy < 100:
#             self.energy += food
#         else:
#             print('Not hungry')
        
#     def do_exercise(self, hours):
#         if self.energy > 0:
#             self.energy -= hours * 2
#             self.power += hours * 2
#         else:
#             print('Too tired')
    
#     def change_alias(self, new_alias):
#         self.alias = new_alias

#     # в методы мы без проблем можем передавать другие объекты и с ними взаимодействовать  
#     def beat_up(self, foe):
#         if not isinstance(foe, Character): # проверка является ли объект экземпляром указанного класса
#             return
#         if foe.power < self.power:
#             foe.status = 'defeated'
#             self.status = 'winner'
#         else:
#             print('Retreat!')
#             foe.status = 'none'
#             self.status = 'none'


# help(print)


# # In[46]:


# peter = Character('Peter Parker', 80)
# bruce = Character('Bruce Wayne', 85)


# # In[47]:


# bruce.beat_up(peter)


# # In[48]:


# print(peter.status)
# print(bruce.status)


# # In[49]:


# peter.beat_up(bruce)


# # In[50]:


# print(peter.status)
# print(bruce.status)

class Person:
    def __init__(self, id):
        self.id = id
some_person = Person(100)
some_person.__dict__['age'] = 30
print(some_person.age + len(some_person.__dict__))