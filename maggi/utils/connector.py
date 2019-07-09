
import subprocess

def dockin(containerid):
    print(u'\u2713',"building vm environment ......")
    # subprocess.run(["docker", "exec", "-ti", containerid, "echo", "setting up vm environment"])
    # print(u'\u2713',"installing dependencies ....")
    # subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
    #                 "update"])
    # subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
    #                 "install", "-y", "curl"])
    # subprocess.run(["docker", "exec", "-ti", containerid, "curl", "-O",
    #                 "https://gist.githubusercontent.com/anuragsarkar97/00b7d342dc9c1fc0b4de57b88d0afe08/raw/0d241fc70157e5c851b6067cd7615052ce4580ca/bamboo-cont.sh"])
    # print(u'\u2713',"setting posix")
    # print(u'\u2713',"running docker instance")
    # subprocess.run(["docker", "exec", "-ti", containerid, "sh",
    #                 "bamboo-cont.sh"])

    print("setup complete ....")

# dockin("instantbox_managed_fJd5HD2eizTuL0yS")