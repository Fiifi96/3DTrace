import subprocess

scripts = ['setup.py', 'map4.py']

for scripts in scripts:
    subprocess.run(['python3', scripts])