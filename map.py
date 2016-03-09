# Author: Dr. Shahin Rostami # Version: 0.1
import os
import sys
import Getch
from random import randint

getch = Getch._Getch()
player_x = 1
player_y = 1
score = 0
level = 1


def beep():
    print "\a"


def spawn_coin(map):
    y = randint(0, len(map) - 1)
    x = randint(0, y)
    while((map[y][x] == "1") or (map[y][x] == "X")):
            y = randint(0, len(map) - 1)
            x = randint(0, y)
    map[y][x] = "C"
    return map


def collect_coin(map, x, y):
    map[x][y] = 0
    beep()
    global score
    score = score + 100
    return map


def load_map(map_location):
    map_file = open(map_location, "r")
    map = []
    for line in map_file:
        map.append(line.strip().split(','))
    map_file.close()
    return map


def draw(map):
    for idx, line in enumerate(map):
        for idy, column in enumerate(line):
            if(idx == player_x and idy == player_y):
                sys.stdout.write("X")
            elif(column == "C"):
                sys.stdout.write("C")
            else:
                sys.stdout.write(column if column == "1" else " ")
        sys.stdout.write("\n")
    sys.stdout.flush()


def controller(key_input, map):
    global player_x
    global player_y
    move_x = 0
    move_y = 0

    if(key_input == "q"):
        exit()
    if(key_input == "s"):
        move_x = 1
    if(key_input == "w"):
        move_x = -1
    if(key_input == "a"):
        move_y = -1
    if(key_input == "d"):
        move_y = 1

    if(map[player_x + move_x][player_y + move_y] == "1"):
        beep()
    else:
        if(map[player_x + move_x][player_y + move_y] == "C"):
            map = collect_coin(map, player_x + move_x, player_y + move_y)
            map = spawn_coin(map)
        player_x = player_x + move_x
        player_y = player_y + move_y

    return map

map = load_map("map_{}.txt".format(level))
spawn_coin(map)
while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    draw(map)
    print "points: {} \t level: {}".format(score, level)
    map = controller(getch(), map)
    if(score >= 500):
        level = level + 1
        map = load_map("map_{}.txt".format(level))
        spawn_coin(map)
        player_x = 1
        player_y = 1
        score = 0
