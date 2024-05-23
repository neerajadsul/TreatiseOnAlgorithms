import random
from dataclasses import dataclass
from string import ascii_letters

def first_name():
    return ''.join(random.choices(ascii_letters, k=6))

def last_name():
    return ''.join(random.choices(ascii_letters, k=6))

def power():
    return random.randint(25, 100)

def effect():
    return random.random()


@dataclass
class RealWorldData:
    first_name: str 
    last_name: str 
    power: int  
    effect: float 

    # def effect(self, value):
    #     if not (0.0 < value < 1.00):
    #         raise ValueError(f'Must be within range [0.0, 1.0], got {value}')

    def __lt__(self, other):
        return self.power * self.effect < other.power * other.effect
        
    def __eq__(self, other):
        return self.power * self.effect == other.power * other.effect

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.power}, {self.effect}'
 