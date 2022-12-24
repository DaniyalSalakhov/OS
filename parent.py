#!/usr/bin/python3
import os
import sys
import random as rnd

def do_fork():
	child_fork = os.fork()
	if child_fork > 0:
		print(f'Parent[{os.getpid()}]: I ran children process with PID {child_fork}')
	else:
		rand_arg = rnd.randint(5, 10)
		os.execl(sys.executable, sys.executable, './child.py', str(rand_arg))
	return child_fork

child_count = int(sys.argv[1])
count = child_count

while child_count > 0:
	child = do_fork()
	if child > 0:
		child_count = child_count - 1

while count > 0:
	child_pid, status = os.wait()
	if status == 0:
		print(f'Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit status {status}.')
		count = count - 1
	else:
		child = do_fork()

os._exit(os.EX_OK)
