## This game will be set in the year 2800 onea majestic planet
## You will be put through multiple rooms and problems that will change how you proceed
## Your goal is to get off this planet and find your way back to Earth
## Welcome to Ethereal
from sys import exit ; from random import randint

class Scene(object):

    def enter(self):
        exit(0)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    pain = [
    "You have died. Better luck next time!",
    "What are you doing man? Try again!",
    "Better luck next time!"
    ]

    def enter(self):
        print(Death.pain[randint(0, len(self.pain)-1)])
        exit(1)

class CrashSite(Scene):

    def enter(self):
        print(" ------------------------------------------------------------  ")
        print("|                                                             |")
        print("|              !!!WELCOME TO PLANET ETHEREAL!!!               |")
        print("|                                                             |")
        print("| You awake to a bright light and someone standing behind it. |")
        print("|   Welcome to planet Ethereal. What is your business here?   |")
        print("|    You relize this creature talking to you is a unicorn.    |")
        print("|      You stand up. You feel a sharp pain in your neck.      |")
        print("|           We suggest you leave our planet at once!          |")
        print("|    You look around, to your left it appears to be a gun,    |")
        print("|        but to your right is the remains of your ship.       |")
        print("|      You have the choice to leave or stand you ground.      |")
        print("|   You take a step back to decide your destiny! Goodluck!    |")
        print("|_____________________________________________________________|")
        print(" 1. Grab the gun!  2. Check the remains.  3. Stand your ground ")

        action = input("> ")

        if action == "1":
            print(" ------------------------------------------------------------  ")
            print("|   You run over towards the Revolver laying on the ground.   |")
            print("|  As you pick up the gun you relize there is no ammo in it!  |")
            print("|          Luckily you spot ammo all over the ground          |")
            print("|       You see in the distance the unicorn watching you.     |")
            print("| You decide to start to pick up the ammo and reload the gun. |")
            print("|     As you look up you see the unicorn charging at you.     |")
            print("|     You load the gun point it at the unicorn and 'click'    |")
            print("|                     The gun is jammed!                      |")
            print("|_____________________________________________________________|")
            return 'death'

        elif action == "2":
            print(" ------------------------------------------------------------  ")
            print("|        You run over towards the remains of your ship.       |")
            print("|  As you get closer you can tell that the ship is destroyed  |")
            print("|   You start to salvage through the parts to find anything   |")
            print("|  You come across serveral differnt items that you can use!  |")
            print("|      There is an EscapePod, a Grenade, and a Survivor.      |")
            print("|           This could be your chance for survival!           |")
            print("|    You start up the EscapePod, grab the grenade and run!    |")
            print("|      As your running you relize you left the survivor!      |")
            print("|_____________________________________________________________|")
            return 'ShipRemains'

        elif action == "3":
            print(" ------------------------------------------------------------  ")
            print("|             You stand tall and taunt the unicorn.           |")
            print("|    The unicorn starts the charge gaining speed every step!  |")
            print("|       You close your eyes and swing as hard as you can.     |")
            print("|      KABOOM! You actually made contact with the unicorn!    |")
            print("|         The unicorn flies back but lands on its feet.       |")
            print("|    This could be your chance to run! But insted you stay.   |")
            print("|       The unicorn bursts torwards you at extreme speed!     |")
            print("|    Before you can even move you relize you made a mistake   |")
            print("|    You look down and see a massive hole through your chest  |")
            print("|_____________________________________________________________|")
            return'death'

        else:
            print("     You stand their in misbelief. Eventually the Unicorn rises up     ")
            print(" A bright beam of light rains from its horn before you can even react. ")
            return'CrashSite'


class ShipRemains(Scene):

    def enter(self):
        print(" ------------------------------------------------------------  ")
        print("|      You stand there debating whether or not to go back     |")
        print("|        You know god wants you to do the right thing.        |")
        print("|_____________________________________________________________|")
        print("     1. Go back and save him!  2. Screw that guy! I'm out!     ")

        action = input("> ")

        if action == "1":
            print(" ------------------------------------------------------------  ")
            print("| You run back and pick up the survivor and begin to run back.|")
            print("||")
            print("|_____________________________________________________________|")
class Finished(Scene):

    def enter(self):
        print("CONGRADULATIONS")

class HoldingChamber(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    scenes = {
        'CrashSite': CrashSite(),
        'HoldingChamber': HoldingChamber(),
        'ShipRemains': ShipRemains(),
        'EscapePod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('CrashSite')
a_game = Engine(a_map)
a_game.play()
