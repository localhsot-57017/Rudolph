
import subprocess

def dockin(containerid,directory,proj_choice):
    print(u'\u2713',"building vm environment ......")
    subprocess.run(["docker", "exec", "-ti", containerid, "echo", "setting up vm environment"])
    print(u'\u2713',"installing dependencies ....")
    subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
                    "update"])
    subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
                    "install", "-y", "curl"])
    subprocess.run(["docker", "exec", "-ti", containerid, "curl", "-O",
                    "https://gist.githubusercontent.com/anuragsarkar97/00b7d342dc9c1fc0b4de57b88d0afe08/raw/0d241fc70157e5c851b6067cd7615052ce4580ca/bamboo-cont.sh"])
    print(u'\u2713',"setting posix")
    print(u'\u2713',"running docker instance")
    subprocess.run(["docker", "exec", "-ti", containerid, "sh",
                    "bamboo-cont.sh"])
    if proj_choice == 1:
        subprocess.run(["docker","exec","-ti", containerid, "curl","-O",
                    "https://gist.githubusercontent.com/redhood-97/daad05a7c0d51dfdc5bb383c24ae7d63/raw/0e499c9739ef478c9ab71b59758c5d558b091aac/docker_spring_env.sh"])
        subprocess.run(["docker", "exec", "-ti", containerid, "sh", "docker_spring_env.sh"])
    elif proj_choice == 2:
        subprocess.run(["docker","exec","-ti",containerid,"pip3","install","flask"])
    elif proj_choice == 3:
        subprocess.run(["docker","exec","-ti",containerid,"apt","install","python"])
        subprocess.run(["docker","exec","-ti",containerid,"apt","install","python-pip"])
        subprocess.run(["docker","exec","-ti",containerid,"pip","install","flask"])
    print(u'\u2713',"Tranferring project folder to the root dir of VM....")
    subprocess.run(["docker", "cp", "-a", directory, containerid + ":/"])

    print("setup complete ....")

# dockin("instantbox_managed_fJd5HD2eizTuL0yS")