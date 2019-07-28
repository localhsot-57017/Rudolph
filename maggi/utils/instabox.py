import os
import subprocess

def cmd_exists(cmd):
    return any(
        os.access(os.path.join(path, cmd), os.W_OK)
        for path in os.environ["docker"].split(os.pathsep)
    )

def serv_exists(cmd):
    return any (os.environ.get('docker')
    )
    
def buildlinux(path = ""):
    print("setting local servers")
    if serv_exists("docker"):
        print("yay docker check")
    else:
        print("docker not found")
        exit(1)
    if serv_exists("docker-compose"):
        print("yay docker-compose check")
    else:
        print("docker not found")
        exit(1)
    if os.path.exists(path + "instantbox") == False :
        os.makedirs(path + "instantbox")
    os.chdir(path + "instantbox")
    print(os.path.exists(path + "instantbox"))
    if not os.path.exists("docker-compose.yml"):
        subprocess.run(["curl", "-sSLO", "https://raw.githubusercontent.com/instantbox/instantbox/master/docker-compose.yml"])
    subprocess.run(["docker-compose", "up", "-d"])
    print("Starting docker machine....")

# buildlinux()