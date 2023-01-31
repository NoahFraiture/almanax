from pynput.mouse import Button, Controller
import time
from numpy import random

def click(pos, mouse):
    mouse.position = pos
    time.sleep(0.05 + random.randint(10)/800)
    mouse.press(Button.left)
    time.sleep(0.001 + random.randint(10)/5000)
    mouse.release(Button.left)
    time.sleep(0.5 + random.randint(10)/50)


def init():
    position = {
        'npc':(940, 558), 
        'line1':(840, 784), 
        'line2':(840, 816), 
        'season':(1250, 400), 
        'summer':(1050, 450), 
        'automn':(1274, 538),
        'stone':(960, 570),
        'outstone':(703, 768),
        'outseason':(751, 793)}
    return Controller(), position

def go(ordre):
    controller, positions = init()
    for pos_name in ordre:
        click(positions[pos_name], controller)
        if pos_name in ("season", "automn", "summer", "winter", "spring", "stone", 'outstone', 'outseason'):
            time.sleep(2.5)

def forward():
    season = "automn"
    ordre1 = ('npc', 'line1', 'line2', 'line2', 'line1', 'npc', 'line1', 'line2', 'season', season, 'stone')
    go(ordre1)

def backward():
    ordre2 = ('outstone', 'outseason', 'npc', 'line1', 'line2')
    go(ordre2)

if __name__ == "__main__":
    ordre1 = ('npc','line1','line2','line2','line1','npc','line1','line2','season', 'automn','stone')
    ordre2 = ('outstone', 'outseason', 'npc', 'line1', 'line2')
    while True:
        step = input("Keske on fait ? ")
        match step:
            case "exit" | "Exit" | "out" | "Out":
                break 
            case "1":
                go(ordre1)
            case "2":
                go(ordre2)
