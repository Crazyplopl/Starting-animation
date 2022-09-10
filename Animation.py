import os
import threading
from itertools import cycle
import sys
from time import sleep as wait

def animatedLoadingScreen():
    #for c in cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
    #for c in cycle(['|', '/', '-', '\\']): # Choose one
    for c in cycle(["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]):
        if done:
            print("\rLoaded!                      ")
            global ready
            ready = True
            sys.exit()
        sys.stdout.write("\rLoading " + c)
        sys.stdout.flush()
        wait(0.1)

os.system('cls' if os.name=='nt' else 'clear')
done = False
ready = False
t = threading.Thread(target=animatedLoadingScreen)
t.daemon = True
t.start()

###Loading Stuff###


wait(10) # Replace with what you need to initialise/load


###################

done = True

os.system('cls' if os.name=='nt' else 'clear')

while not ready:
    wait(1)
os.system('cls' if os.name=='nt' else 'clear')
print("Loaded!")

#Your program here