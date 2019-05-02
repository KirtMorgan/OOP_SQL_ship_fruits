from db_connection_wrapper import *
from fruit import Fruit

class Boat:
    def __init__(self, name='', current_location='', destination=''):
        self.name = name
        self.current_location = current_location
        self.destination = destination
        self.cargo_list = []

    def sail(self):
        print(f'Sailing from {self.current_location} to {self.destination}')


