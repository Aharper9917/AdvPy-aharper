'''
https://open.kattis.com/problems/glitchbot
'''
def test():
    coords1 = [3, 2]
    instructs1 = ['forward', 'right', 'forward', 'forward', 'left', 'forward', 'forward', 'left', 'forward', 'right', 'forward']
    coords2 = [-1, 1]
    instructs2 = ['right', 'left', 'forward']

    assert(checkPosEquality(coords2, instructs2) == "1 forward")
    assert(checkPosEquality(coords1, instructs1) == "8 right")

def changeDir(currDir, turn):
    directions = ['north', 'east', 'south', 'west']
    turns = {
        'right':  1,
        'left' : -1 
    }
    dirs = {
        'north': 0,
        'east' : 1,
        'south': 2,
        'west' : 3 
    }

    currDir = dirs[currDir]
    turn = turns[turn]

    if(currDir + turn == 4):
        d = directions[0]
    else:
        d = directions[currDir + turn]

    return d

def move(pos, dir):
    directions = ['north', 'east', 'south', 'west']
    dirs = {
        'north': [ 0, 1],
        'east' : [ 1, 0],
        'south': [ 0,-1],
        'west' : [-1, 0]
    }
    pos = [x + y for x, y in zip(pos, dirs[dir])]
    return pos

def run(instructions):
    pos = [0, 0]
    direction = 'north'

    for instruction in instructions:
        if(instruction == 'right' or instruction == 'left'):
            direction = changeDir(direction, instruction)
        elif(instruction == 'forward'):
            pos = move(pos, direction)

    return pos

def checkPosEquality(coords, instructions):
    steps = ['forward', 'left', 'right']

    for i in range(len(instructions)):
        x = instructions[i]
        for step in steps:
            instructions[i] = step
            if (run(instructions) == coords):
                return (str(i+1) + " " + str(step))
            else:
                continue 
        instructions[i] = x

def main():
    test()
    coords = [int(coord) for coord in input().split(' ')]
    instructions = [input().lower() for i in range(int(input()))]
    print(checkPosEquality(coords, instructions))

if __name__ == "__main__":
    main()
