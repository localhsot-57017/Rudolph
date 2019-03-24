import os
import subprocess

def cmd_exists(cmd):
    return any(
        os.access(os.path.join(path, cmd), os.X_OK)
        for path in os.environ["PATH"].split(os.pathsep)
    )

def buildlinux(path = ""):
    print("setting local servers")
    if cmd_exists("docker"):
        print("yay docker check")
    else:
        print("docker not found")
        exit(1)
    if cmd_exists("docker-compose"):
        print("yay docker-compose check")
    else:
        print("docker not found")
        exit(1)
    if not os.path.exists(path + "instantbox"):
        os.makedirs(path + "instantbox")
    os.chdir(path + "instantbox")
    if not os.path.exists("docker-compose.yml"):
        subprocess.run(["curl", "-sSLO", "https://raw.githubusercontent.com/instantbox/instantbox/master/docker-compose.yml"])
    subprocess.run(["docker-compose", "up", "-d"])
    print("starting docker machine")

# buildlinux()