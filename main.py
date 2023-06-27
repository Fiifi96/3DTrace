import subprocess

scripts = ['setup.py', 'map.py']

for scripts in scripts:
    subprocess.run(['python3', scripts])