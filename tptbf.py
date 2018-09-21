from os import system
from sys import argv
import time

def tptbf(n_hours=1):
    for i in range(n_hours):
        for j in range(5):
            system('say "start working for 10 minutes"')
            time.sleep(9*60)
            system('say "one minute of work left... wrap it up"')
            time.sleep(1*60)
            system('say "do what you want for 2 minutes"')
            time.sleep(90)
            system('say "thirty seconds left"')
            time.sleep(0.5)
            system('say "get ready to get back to work"')
            time.sleep(29.5)
    system('say "you\'re done. you\'ve completed {} hours of ten plus two by five."'.format(n_hours))

if len(argv) > 1:
    n_hours = int(argv[1])
else:
    n_hours = 1
tptbf(n_hours)
