# Inheritance vs Composition


"""

Inheritance

"""


class Engine:
    def start_engine(self):
        print("Engine started.")


class MusicSystem:
    def play_music(self):
        print("Playing music.")


class Car(Engine, MusicSystem):
    pass


my_car = Car()
my_car.start_engine()
my_car.play_music()

"""

Composition



"""


class Engine:
    def start(self):
        print("Engine started.")


class MusicSystem:
    def play(self):
        print("Playing music.")


class Car:
    def __init__(self):
        self.engine = Engine()
        self.music_system = MusicSystem()

    def start_car(self):
        self.engine.start()

    def play_music(self):
        self.music_system.play()


""""
Inheritance: is-a relationship. 
Composition: has-a relationship
"""
