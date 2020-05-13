import argparse
import keyboard
import random 
import time
import csv
import gol

class Pauser():
    _running = True
    def toggle(self, e):
        self._running = not self._running
        print("Paused!")
    
    @property
    def running(self):
        return self._running

pauser = Pauser()

N=[30,30]
parser = argparse.ArgumentParser(usage="python pygol [-f FILE]", description="Game of Life")
parser.add_argument('-f' , '--file', dest='filename', help='Filename of the initial world configuration.')
args = parser.parse_args()

# Initialize world
filename = args.filename        
world = []
if(filename != None):
    #Use file to initialize
    print("Using initial config file.")
    with open(filename, 'r') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        try:
            world=[list(map(int,rec)) for rec in data]
        except ValueError:
            print("Invalid elements in "+filename)
            exit()
else:
    #Randomly initialize
    print("Random initialization.")
    for i in range(0,N[0]):
        row = []
        for j in range(0,N[1]):
            state = random.randint(0,10)
            if state>9:
                row.append(1)
            else:
                row.append(0)
        world.append(row)
# Check if world dimensions are valid
if (gol.check_world_dim(world)):
    keyboard.on_press_key("space", pauser.toggle)
    try:
        tick = 0
        gol.display(world)
        print("Initial State!")
        print("Press Space to start...")
        while(True):
            if(pauser.running):        
                world = gol.next(world)
                tick += 1
                gol.display(world)
                print("Tick #: "+str(tick))
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n\nExiting Game of Life!\n\n")
        exit()


    