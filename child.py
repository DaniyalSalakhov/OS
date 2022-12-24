import os
import sys
import time
import random as rnd

s = int(sys.argv[1])
print(f'Child[{os.getpid()}]: I am started. My PID {os.getpid()}. Parent PID {os.getppid()}.')
time.sleep(s)
print(f'Child[{os.getpid()}]: I am ended. PID {os.getpid()}. Parent PID {os.getppid()}.')
status = rnd.randint(0, 1)
os.exit(status)
