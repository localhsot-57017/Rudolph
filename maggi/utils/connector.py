
import subprocess

def dockin(containerid):
    print(u'\u2713',"building vm environment ......")
    subprocess.run(["docker", "exec", "-ti", containerid, "echo", "setting up vm environment"])
    print(u'\u2713',"installing dependencies ....")
    subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
                    "update"])
    subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
                    "install", "-y", "curl"])
    subprocess.run(["docker", "exec", "-ti", containerid, "curl", "-O",
                    "https://gist.githubusercontent.com/anuragsarkar97/00b7d342dc9c1fc0b4de57b88d0afe08/raw/29009a2924914f7287897ae68241088bebcb9838/maggi-cont.sh"])
    print(u'\u2713',"setting posix")
    print(u'\u2713',"running docker instance")
    subprocess.run(["docker", "exec", "-ti", containerid, "sh",
                    "maggi-cont.sh"])
    print(u'\u2713',"building security env ...")
    # subprocess.run(["docker", "exec", "-ti", containerid,
    #                 "rm", "-rf", "katoolin"])
    # subprocess.run(["docker", "exec", "-ti", containerid,
    #                 "git", "clone", "http://github.com/LionSec/katoolin.git"])
    # subprocess.run(["docker", "exec", "-ti", containerid,
    #                 "cp", "katoolin/katoolin.py", "/usr/bin/katoolin"])
    # subprocess.run(["docker", "exec", "-ti", containerid,
    #                 "chmod", "+x", "/usr/bin/katoolin"])
    # subprocess.run(["docker", "exec", "-it", containerid,
    #                 "katoolin"])

    print("setup complete ....")


# dockin("instantbox_managed_fJd5HD2eizTuL0yS")