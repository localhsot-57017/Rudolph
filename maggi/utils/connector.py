
import subprocess

def dockin(containerid, framework):
    print(u'\u2713',"building vm environment ......")
    subprocess.run(["docker", "exec", "-ti", containerid, "echo", "setting up vm environment"])
    print(u'\u2713',"installing dependencies ....")
    subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
                    "update"])
    subprocess.run(["docker", "exec", "-ti", containerid, "apt-get",
                    "install", "curl"])
    if framework == 'java:spring-boot':
        subprocess.run(["docker", "exec", "-ti", containerid, "apt-get", "install","install openjdk-8-jdk" ])
        subprocess.run(["docker","exec","-ti", containerid, "curl","-O",
                    "https://gist.githubusercontent.com/redhood-97/daad05a7c0d51dfdc5bb383c24ae7d63/raw/02d484a79652396e12b4d502e047f94a0c5aeae4/docker_spring_env.sh"])
        subprocess.run(["docker", "exec", "-ti", containerid, "sh", "docker_spring_env.sh"])
    elif framework == 'python3:Flask':
        subprocess.run(["docker", "exec", "-ti", containerid, "pip3",
                    "install", "flask"])
    elif framework == 'python2:Flask':
        subprocess.run(["docker", "exec", "-ti", containerid, "apt",
                    "install", "python"])
        subprocess.run(["docker", "exec", "-ti", containerid, "apt",
                    "install", "python-pip"])
        subprocess.run(["docker", "exec", "-ti", containerid, "pip",
                    "install", "flask"])
        
    print("setup complete ....")

# dockin("instantbox_managed_fJd5HD2eizTuL0yS")