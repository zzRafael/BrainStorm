import subprocess

def executor():
    subprocess.call(["python", "C:\Users\User\Documents\GitHub\BrainStorm\subprocess_test\exe\dist\counter.exe"])

exe_number = 5

for i in range(exe_number):
    executor()
