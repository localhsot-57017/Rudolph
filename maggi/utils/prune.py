import subprocess

def prune():
    subprocess.run(["docker", "system", "prune", "--volumes" , "-a"])