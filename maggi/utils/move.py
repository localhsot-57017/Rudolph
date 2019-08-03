import os 
import subprocess


def copy(directory_path, docker_id):
  print("copying data to VM")
  docker_absolute_path = docker_id + ":."
  subprocess.run(['docker', 'cp', directory_path , docker_absolute_path])


def start(containerid, directory, file2run, framework):
  file = directory.split('/')[-1]
  print(file)
  subprocess.run(["docker", "exec", "-ti", containerid, "-w",
                    file])
  if framework == 'java:spring-boot':
    subprocess.run(["docker", "exec", "-ti", containerid, "mvn",
                    "spring-boot:run"])
  elif framework == 'python3:Flask':
    subprocess.run(["docker", "exec", "-ti", containerid, "python3",
                    file2run])
  elif framework == 'python2:Flask':
    subprocess.run(["docker", "exec", "-ti", containerid, "python",
                    file2run])  
    
# copy("/Users/oyo/Desktop/a.cpp", "anurag.sarkar1@10.15.14.22:")


## TODO : instruction.yml -==== build script