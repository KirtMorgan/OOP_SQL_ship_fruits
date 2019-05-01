from boat import Boat
from fruit import Fruit
boat = Boat('SS Longboat', 'Britain', 'America')
fruit1 = Fruit('Apple', 10)
fruit2 = Fruit('Orange', 5)
fruit3 = Fruit('Pineapple', 15)

boat.add_cargo(fruit1)
boat.add_cargo(fruit2)
boat.add_cargo(fruit3)

boat.print_cargo_list()
