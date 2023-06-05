# print(type('hello world'))

# class Character: # создали класс 'Character'
#     pass

# peter = Character() # создали экземпляр класса
# print(type(peter))

# добавим классу атрибутов
class Character: 
    name = 'some name'
    power = 0
    energy = 100
    hands = 2

# при вызвое класса мы всегда создаём новый объект 
# у конкретного экземпляра будут все теже атрибуты, что и у его класса
peter = Character()
print(peter.name)
print(peter.power)
print(peter.energy)
print(peter.hands)

# мы можем экземпляру присвоить свои атрибуты
peter.name = 'Peter Parker'
peter.power = 70
# и даже те, которых изначально нет в самом классе
peter.alias = 'Spider-Man'
print(peter.alias)