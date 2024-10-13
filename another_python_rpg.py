# Player: - Stats: Int, Luck, Energy, Money
# - Inventory?
# Actions: Sleep, Study, Work - Actions consume energy for gain
# Store: Buy Items for Stat buff

import random

class Player:
    name = None
    energy = 100
    money = 10000
    prestige = 0
    intelligence = None
    luck = None
    items = []

    @staticmethod
    def generate_random_stat(min = 30, max = 60):
        return random.randint(min, max)
    
    @classmethod
    def display_player_stats(cls):
        print(f'Energy: {Player.energy}')
        print(f'Money: {Player.money}')
        print(f'Intelligence: {Player.intelligence} | Luck: {Player.luck} | Prestige: {Player.
        prestige}')
        print('Inventory:')
        for index, item in enumerate(cls.items, start = 0):
            print(f'{index} - {item.name}')

    @classmethod
    def update_stats(cls):
        for item in cls.items:
            cls.prestige += item.prestige
            cls.intelligence += item.intelligence
            cls.luck += item.luck
    
    @classmethod
    def add_items(cls, item):
        cls.items.append(item)
        cls.update_stats()


class Item:
    def __init__ (self, name, price, energy = None, prestige = None, intelligence = None, luck = None):
        self.name = name
        self.price = price
        self.energy = energy
        self.prestige = prestige
        self.intelligence = intelligence
        self.luck = luck

 
class Store:
    items = []

    @classmethod
    def visit_store(cls):
        print(f'Shopkeeper: Good day {Player.name}!')
        print('Items for sale:')
        for index, item in enumerate(cls.items, start = 0):
            print(f'{index} - Item: {item.name}, Price: {item.price}, Energy: {item.energy}, Prestige: {item.prestige}, Intelligence: {item.intelligence}, Luck: {item.luck}')
        print(f'Money: {Player.money}')
        response = None

        while response != 'q':
            response = input("What would you like to purchase (Input the Item's Index Number) or 'q' to exit store")
                
            if response == 'q':
                print('Exiting the store.')
                break
            
            try:
                select_item = int(response)    
            except ValueError:
                print('Please input an Item Index Number')
                continue
            if 0 <= select_item < len(cls.items):
                item = cls.items[select_item]
                if Player.money > item.price:
                    Player.money -= item.price
                    Player.add_items(item)
                    print(f'You bought {item.name}')
                    print(f'Money: {Player.money}')
                    break
                else:
                    print('Not enough money')
                    continue
            else:
                print('item does not exist')

class Game:
    def run(self):
        Player.name = input('Input your name')
        Player.intelligence = Player.generate_random_stat()
        Player.luck = Player.generate_random_stat()
        print(f'Player: {Player.name} created')
        Player.display_player_stats()
        Game.initialize_items()
        print('Items initialized:', [item.name for item in Store.items])

        while True: 
            action = input("What do you do? 'sleep', 'study, 'work', 'store', 'stats', quit")
            match action:
                case 'sleep':
                    Player.energy = 100
                    print('You feel refreshed! Energy restored to 100!')
                case 'study':
                    Player.intelligence += 5
                    Player.energy -= 50
                    print('You feel a little tired after studying, but a little more confident in your abilities!')
                case 'work':
                    Player.energy -= 50
                    money_gained = random.randint(500, 1500)
                    Player.money += money_gained
                    print('You feel a little tired after working')
                    print(f'You made {money_gained}')
                case 'store':
                    print('You visit the store')
                    Store.visit_store()
                case 'stats':
                    Player.display_player_stats()
                case 'quit':
                    print('Exiting the game')
                    break
                case _:
                    print('Action not possible, please try again')
        
    @classmethod
    def initialize_items(cls):
        shades = Item("Black Shades", 500, 0, 10, 0, 10)
        charm = Item("Four Leaf Clover", 1000, 0, 0, 0, 50)
        iphone = Item("IPhone 20 Pro Max", 5000, -25, 50, -10, -5)
        Store.items.extend([shades, charm, iphone])


game = Game()
game.run()
