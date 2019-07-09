import os 
import subprocess


def copy(directory_path, docker_id):
    print("copying data to VM")
    docker_absolute_path = docker_id + ":."
    subprocess.run(['docker', 'cp', directory_path , docker_absolute_path])

# copy("/Users/oyo/Desktop/a.cpp", "anurag.sarkar1@10.15.14.22:")


## TODO : instruction.yml -==== build script