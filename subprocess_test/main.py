import subprocess

def executor():
    subprocess.call(["Python", "subprocess_test\\exe\\dist\\counter.exe"])

exe_number = 5

for i in range(exe_number):
    executor()
